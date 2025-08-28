import HookBase

# Please use this hook class with the faster r-cnn and retinanet notebooks only, copy paste this hook class to the hook section in the notebook.
''' 
This hook reports the validation loss inclusive with the warmup phase, however its logic remains the same which is early stopping ONLY after warmup phase. 
So, its pretty much the same as the hook existing in faster r-cnn and retinanet notebooks just a difference in validation loss reporting.
'''

class LossHook(HookBase):
    def __init__(self, cfg, is_validation=False):
        super().__init__()
        self.cfg = cfg.clone()
        self.cfg.DATASETS.TRAIN = self.cfg.DATASETS.TEST if is_validation else self.cfg.DATASETS.TRAIN
        self._loader = iter(build_detection_train_loader(self.cfg))
        self.loss_prefix = "val_" if is_validation else "train_"
        self.total_images = 40
        self.total_loss = 0
        self.total_batches=0
        self.patience=5
        self.no_improvements = 0
        self.best_val_loss = float('inf')
        self.is_validation = is_validation
        self.prev_epoch = 0
        self.prev_loss = 0
        self.iter_count = 0
        self.iters_per_epoch = self.total_images // self.cfg.SOLVER.IMS_PER_BATCH
        self.warmup_epoch = self.cfg.SOLVER.WARMUP_ITERS/self.iters_per_epoch

    def after_step(self):
        data = next(self._loader)
        with torch.no_grad():
            loss_dict = self.trainer.model(data)
            losses = sum(loss_dict.values())
            assert torch.isfinite(losses).all(), loss_dict
            loss_dict_reduced = {self.loss_prefix + k: v.item() for k, v in comm.reduce_dict(loss_dict).items()}
            losses_reduced = sum(loss for loss in loss_dict_reduced.values())
            self.total_loss += losses_reduced
            self.total_batches += 1
            self.iter_count += 1
            average_loss = self.total_loss / self.total_batches

        if self.total_batches>0 and comm.is_main_process() and self.iter_count==self.iters_per_epoch:
          epoch = math.ceil(self.trainer.iter / self.iters_per_epoch)
            
          if self.prev_epoch!= epoch:
              self.prev_epoch = epoch
              self.prev_loss = average_loss
              print(f"{self.loss_prefix.capitalize()}Loss (Epoch {int(self.prev_epoch)}): {self.prev_loss:.4f}")

          if self.trainer.iter > self.cfg.SOLVER.WARMUP_ITERS:
            if self.is_validation:
              if average_loss < self.best_val_loss:
                self.best_val_loss = average_loss
                self.no_improvements = 0
              else:
                self.no_improvements += 1

            if self.no_improvements >= self.patience:
                checkpointer = DetectionCheckpointer(self.trainer.model, save_dir=self.cfg.OUTPUT_DIR)
                checkpointer.save("Insert any model .pth file name")
                raise StopIteration("Early Stopping Trigerred")

          self.total_loss = 0
          self.total_batches=0
          self.iter_count=0
