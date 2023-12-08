## Training Details of Open-Source Models
Our analysis utilizes two types of training datasets for the eight pedestrian detectors. General object detectors, including YOLOX, RetinaNet, Faster RCNN, and Cascade RCNN, are trained using the MS COCO training dataset (https://mmdetection.readthedocs.io/en/latest/model_zoo.html). Pedestrian-specific detectors are trained on the Citypersons datasets (https://paperswithcode.com/dataset/citypersons). Below link is the detailed specifications of these training datasets:

| Name                             | Total Images | Images with Pedestrians | Pedestrian Bounding Boxes |
|----------------------------------|--------------|-------------------------|--------------------------|
| MSCOCO Training Set              | 118,287      | 64,115                  | 262,465                  |
| CityPersons Training Set         | 2,975        | 2,975                   | 19,654                   |


To further investigate the distribution of sensitive attributes in different training datasets, we annotate person instances in these datasets. Given the extensive number of label instances in training datasets, we randomly select a statistically significant sample with a 95% confidence level and a margin of error of ±5%. 

From the MSCOCO training set's 64,115 pedestrian-containing images, our refined dataset included 382 images. Likewise, from the CityPersons training set, we derive a final dataset of 341 images. Below, we present detailed information on the age, gender, and skin-tone of pedestrians instances in each dataset:

<img width="700" alt="image" src="https://github.com/FairnessResearch/Fairness-Testing-of-Autonomous-Driving-Systems/assets/140967709/753bdb5a-bfa2-4054-b4a8-cf983ff7f102">


<img width="700" alt="image" src="https://github.com/FairnessResearch/Fairness-Testing-of-Autonomous-Driving-Systems/assets/140967709/dce0f366-5838-4f35-a7d9-35e87389e94c">
