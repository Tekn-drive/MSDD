# Mini-mart Shelf Detection Dataset
MSDD (Mini-mart Shelf Detection Dataset) is a dataset consisting of 300 shelf images containing nearly 14,000 product instances with more than 100 unique SKUs, each with their own class labels. The dataset is further divided into six broad categories which are cookies, biscuits, oil, milk, coffee, and candy. A comparison in performance between RetinaNet with ResNet101, Faster R-CNN, YOLOS based ViT, and YOLOv11 object detection models is conducted with this dataset.

#### Important: for the hook class that is used by RetinaNet and Faster R-CNN for early stopping, it prints "Val_Loss (Epoch X)" the epoch X here means the non warmup epoch number so suppose the model stopped training at Epoch 7, it doesn't mean it stop at Epoch 7, it stops at the 7th epoch that's not part of the warmup (considering there is 40 training images, batch size of 4, and Detectron2's default warmup iterations which is 1000, therefore the iterations per epoch is 40 images/batch size of 4 = 10 iterations/epoch which means 1000 iterations for warmup/10 iterations per epoch = 100 warmup epochs) So, if the hook said Epoch X it means that the model stopped training at epoch 100 + X (inclusive with warmup epoch). In this case, if X is 7 this means it stopped training at the 107th epoch (inclusive with warmup epoch)

# Model Performance Results
Model performance at mAP50
| Category | YOLOS | RetinaNet with ResNet-101 | Faster R-CNN | YOLOv11 |
|:-------------:|:--------------:|:--------------:|:------------:|:------------:|
| Cookies | 44.5% | 62.39% | 68.08% | 63.51% |
| Biscuits | 48% | 67.83% | 75.73% | 68.35% |
| Oil | 59.7% | 77.44% | 82.3% | 80.63% |
| Milk | 30.3% | 70.13% | 76.23% | 75.24% |
| Coffee | 66.2% | 80.36% | 84.05% | 88.21% |
| Candy | 55.1% | 72.31% | 70.28% | 72.22% |
| Average | 50.63% | 71.74% | 76.11% | 74.69% |

Model performance at mAP50-95
| Category | YOLOS | RetinaNet with ResNet-101 | Faster R-CNN | YOLOv11 |
|:-------------:|:--------------:|:--------------:|:------------:|:------------:|
| Cookies | 23.6% | 42.18% | 45.64% | 47.39% |
| Biscuits | 25.6% | 52.68% | 52.62% | 54.14% |
| Oil | 31% | 57.94% | 58.36% | 65.72% |
| Milk | 24.9% | 55.28% | 56.16% | 62.57% |
| Coffee | 43.1% | 61.56% | 62.26% | 69.38% |
| Candy | 28.1% | 51.96% | 48.04% | 51.44% |
| Average | 29.38% | 53.6% | 53.85% | 58.44% |
