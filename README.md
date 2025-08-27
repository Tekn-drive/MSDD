# Mini-mart Shelf Detection Dataset
A comparison in performance between RetinaNet with ResNet101, Faster R-CNN, YOLOS based ViT, and YOLOv11 object detection models when it comes to identifying products on mini market shelves.

#### Important: for the hook class that is used by RetinaNet and Faster R-CNN for early stopping, it prints "Val_Loss (Epoch X)" the epoch X here means the non warmup epoch number so suppose the model stopped training at Epoch 7, it doesn't mean it stop at Epoch 7, it stops at the 7th epoch that's not part of the warmup (considering there is 40 training images, batch size of 4, and Detectron2's default warmup iterations which is 1000, therefore the iterations per epoch is 40 images/batch size of 4 = 10 iterations/epoch which means 1000 iterations for warmup/10 iterations per epoch = 100 warmup epochs) So, if the hook said Epoch X it means that the model stopped training at epoch 100 + X (inclusive with warmup epoch). In this case, if X is 7 this means it stopped training at the 107th epoch (inclusive with warmup epoch)

# Model Performance Results
Model performance at mAP50
| Category | YOLOS | RetinaNet with ResNet-101 | 
|:-------------:|:--------------:|:--------------:|
| Data 1       | Data 2         | Data 3        |
| Another Row  | More Data      | Last Piece    |

Model performance at mAP50-95
| Category | YOLOS | RetinaNet with ResNet-101 | 
|:-------------:|:--------------:|:--------------:|
| Data 1       | Data 2         | Data 3        |
| Another Row  | More Data      | Last Piece    |
