The authors introduce the **OPEDD: Off-Road Pedestrian Detection Dataset** for pedestrian detection which consists of 1020 images showing varying numbers of persons in differing non-urban environments and comes with manually annotated pixel-level segmentation masks and bounding boxes. It shows significant occlusion of persons from vegetation, crops, objects or other pedestrians. In dataset every image comes with manually created ground truth pixel-level segmentation masks and individual ***person id*** for every portrayed pedestrian, allowing the data to be used for tasks like object detection (bounding boxes), semantic segmentation (pixel masks) or instance segmentation (pixel masks and ***person id***).

Note, similar **OPEDD: Off-Road Pedestrian Detection Dataset** dataset is also available on the [DatasetNinja.com](https://datasetninja.com/):

- [OFFSED: Off-Road Semantic Segmentation Dataset](https://datasetninja.com/offsed)

## Motivation

The identification of pedestrians is a crucial aspect in the advancement of automated driver assistance systems. Existing datasets for pedestrian detection predominantly center around urban settings. However, contemporary neural networks, trained on such datasets, encounter challenges in extending their predictions from one environment to visually distinct ones, limiting their applicability to urban scenes. Commercial working machines, including tractors and excavators, constitute a significant proportion of motorized vehicles and are often situated in vastly different surroundings such as forests, meadows, construction sites, or farmland. These industrial vehicles operate in environments that differ substantially from urban settings. Despite their widespread use in various industries, from robust earthwork operations to precise harvesting, and despite comprising a substantial portion of the motorized vehicle fleet, there is a notable dearth of published datasets specifically tailored for pedestrian detection in these contexts.

Neural networks trained on urban-centric images often struggle to generalize effectively when confronted with non-urban environments. This limitation adversely impacts the detection capabilities of such networks in off-road scenarios, presenting a challenge for Advanced Driver Assistance Systems (ADAS) applied to mobile working vehicles, like automated emergency brakes for tractors, excavators, or harvesters. Moreover, urban environments restrict the diversity of pedestrian poses captured in datasets, with most pedestrians depicted walking or standing upright on pavements. In contrast, industrial or agricultural vehicles operating in off-road environments may encounter people in unconventional poses, such as crouching or lying down while engaged in crop harvesting or construction work. These variations pose safety challenges for humans around autonomously operating vehicles in non-urban contexts.

## Characteristics of Off-Road Environments

Off-road, agricultural or rural environments show several characteristics that differentiate them from urban surroundings in a number of ways:

* **Visuals** The largest differences are recognizable in the visual domain. In urban images, the background is mostly characterized by buildings and paved roads, yielding a colour spectrum dominated by greys. In contrast, off-road environments can depict a multitude of backgrounds. Agricultural and wooded surroundings usually show ample vegetation with a colour spectrum controlled by greens and browns, while construction sites display a mix of urban and non-urban components. In terms of texture, backgrounds dominated by vegetation show heavy textural repetition.

* **Composition** In urban settings, pedestrians are one visually distinct object class out of many, including cars, cyclists, trucks and many more. In off-road environments, pedestrians tend to appear as much more strongly separated objects.

* **Occlusion** In surroundings dominated by vegetation partial occlusion of persons by leaves, grass or branches is very common. Examples are people harvesting fruit in orchards or a person standing in field crops, having parts of the lower body obstructed. Additionally, the boundary of occlusions is often much fuzzier than in the case of occlusions by e.g. cars in the urban setting.

<img src="https://github.com/dataset-ninja/opedd/assets/120389559/f10a2396-7d1d-48ac-8e7a-d38b2a61b5ee" alt="image" width="1000">

<span style="font-size: smaller; font-style: italic;">Dataset shows different types of occlusion in varying environments, including naturally occurring obstacles (left: vegetation, center: construction materials) and unusual objects (right: umbrella).</span>

* **Poses** Due to the nature of city scenes, datasets for pedestrian detection in urban environments show persons predominantly standing or walking upright. Additionally, because the data is usually captured from a vehicle driving on the road, most pedestrians are located on the lateral edges of the image, with persons only directly in front of the camera if the data-capturingvehicle is positioned in front of a cross- or sidewalk. Contrary to that, many agricultural or industrial scenes show persons in unusual and more challenging poses: often the person is seen working in a crouching or bent position and limbs extended in differing ways are common. Due to the hazardous environment on construction sites, the vehicle could encounter people lying on the ground. In general, off-road scenes display a much larger variety of poses than the average urban scene.

<img src="https://github.com/dataset-ninja/opedd/assets/120389559/486b9717-d171-4312-84fe-c9d7b8468d2f" alt="image" width="1000">

<span style="font-size: smaller; font-style: italic;">Special attention was paid to capture a wide range of poses not usually encountered in urban driving datasets. Left: Handstand. Center: Jumping with extended limbs. Right: Head covered with clothes.</span>



## Dataset description

The authors record all sequences of our dataset using a Stereolabs ZED Camera. The stereo camera has a baseline of 120mm and is able to capture video sequences with a side-by-side output resolution of 4416x1242 pixels at 15 frames per second. In order to prevent compression artifacts, which can impair detection performance, the video sequences are captured with lossless compression.  Data was captured in short video sequences of 1 to 50 seconds with a framerate of 15 Hz.

* **Environments** The authors capture data in different locations to cover a broad range of possible ADAS application scenarios: meadows, woods, construction sites, farmland and paddocks. While capturing, emphasis was laid on covering many scenarios that complicate pedestrian detection in offroad environments.

* **Occlusions** In all of environments, occlusion happens with locally characteristical obstacles like grass, leaves, field crops, construction materials or fences, as well as more unusual barriers like stone walls, garbage bins or objects held by persons (umbrellas, paper files). Moreover, the authors took care to include many instances of person-to-person occlusion, oftentimes by a pedestrian standing close to the camera.

* **Poses**  Dataset shows a variety of uncommon and challenging poses including people doing handstands, lying on the ground or on objects, lying on the back or
on the side, sitting, crouching or bent over, limbs extended as well as running and jumping.

* **Composition** Special attention was paid to have multiple positions in the image covered by pedestrians, to avoid the urban situation where persons are located mainly at the sides. Additionally the authors vary the number of persons and the distances they appear to the camera. Most images are taken from eye-level up to 1m above, facing forward, to simulate taller vehicles like tractors or excavators, with images showing a more downward facing angle.

<img src="https://github.com/dataset-ninja/opedd/assets/120389559/714e637d-155e-48bc-8157-4faa26bfb2e1" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">Histogram of distances of the portrayed pedestrians to the camera.</span>

<img src="https://github.com/dataset-ninja/opedd/assets/120389559/aca87536-9445-47d9-bfc9-9bc8866ff1a4" alt="image" width="500">

<span style="font-size: smaller; font-style: italic;">Histogram depicting how many pedestrians are visible in the images.</span>

* **Lighting** The light conditions vary naturally as well as intentionally, with some images being taken against direct sunlight or with people being hidden in the shadows of walls or trees.

<img src="https://github.com/dataset-ninja/opedd/assets/120389559/b348689a-70c4-4d62-a9b6-bf05563781b7" alt="image" width="1000">

<span style="font-size: smaller; font-style: italic;">Samples of images with difficult lighting conditions.</span>

* **Miscellaneous** Further variations include clothing, helmets or gimmicks like clothes being thrown around or people deliberately hiding.

* **Image Selection** From the video sequences 1020 image pairs are selected. Since the images are often almost identical from one frame to the next, the authors make sure to choose the next frame in such a way that sufficient alteration is visible, often by clear repositioning of persons or after a pan of the camera. The images that make it to the final dataset are selected by hand.

* **Annotation** The ground truth annotations of the images were created using the [OPVGG Image Annotation Tool (VIA)EDD](https://www.v7labs.com/). All visible persons were annotated with a segmentation mask and given an  ***person id***. All labelling information is stored in a json file that can also be imported as a VIA project, allowing users to easily modify and expand on the annotations.




