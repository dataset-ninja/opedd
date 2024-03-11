**OPEDD: Off-Road Pedestrian Detection Dataset** is a dataset for instance segmentation, semantic segmentation, object detection, identification, and stereo depth estimation tasks. It is used in the automotive industry. 

The dataset consists of 2038 images with 2800 labeled objects belonging to 1 single class (*person*).

Images in the OPEDD dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 1034 (51% of the total) unlabeled images (i.e. without annotations). There are 2 splits in the dataset: *left* (1020 images) and *right* (1018 images). Additionally, labels contain ***person id*** tag. Explore it in supervisely labeling tool. The dataset was released in 2021 by the <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">University of Kaiserslautern, Germany</span>.

<img src="https://github.com/dataset-ninja/opedd/raw/main/visualizations/poster.png">
