**OPEDD: Off-Road Pedestrian Detection Dataset** is a dataset for instance segmentation, semantic segmentation, object detection, and identification tasks. It is used in the automotive industry. 

The dataset consists of 1020 images with 4190 labeled objects belonging to 1 single class (*person*).

Images in the OPEDD dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 16 (2% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Additionally, labels contain ***person id*** tag. Explore it in supervisely labeling tool. The dataset was released in 2021 by the University of Kaiserslautern, Germany.

<img src="https://github.com/dataset-ninja/opedd/raw/main/visualizations/poster.png">
