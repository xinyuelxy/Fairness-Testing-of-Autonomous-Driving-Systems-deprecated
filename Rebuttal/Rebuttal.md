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


## Results for Intersectional Groups

We also expand our analysis to include intersectional groups. Notably, we compare the miss rates for dark-skin females vs. light-skin males, and dark-skin children vs. light-skin adults. The detailed results are shown below.


| Detectors    | MR DS-female | MR LS-male | EOD         | MR DS-child | MR LS-adult | EOD         |
|--------------|--------------|------------|-------------|-------------|-------------|-------------|
| yolox        | **0.2969**   | **0.0292** | **-0.2676** | **0.1429**  | **0.0432**  | **-0.0997** |
| retinanet    | **0.3073**   | **0.0468** | **-0.2605** | 0.1429      | 0.0611      | -0.0817     |
| faster rcnn  | 0.0156       | 0.0249     | 0.0092      | 0.0476      | 0.0329      | -0.0147     |
| cascade rcnn | 0.0208       | 0.0227     | 0.0018      | 0.0476      | 0.0325      | -0.0151     |
| csp          | **0.0208**   | **0.5431** | **0.5223**  | 0.6667      | 0.5838      | -0.0829     |
| mgan         | **0.5990**   | **0.4671** | **-0.1319** | 0.4762      | 0.4940      | 0.0178      |
| alfnet       | 0.3698       | 0.3553     | -0.0145     | 0.3333      | 0.3859      | 0.0526      |
| prnet        | 0.5104       | 0.5336     | 0.0232      | 0.6190      | 0.5568      | -0.0622     |
| overall      | 0.2676       | 0.2528     | -0.0147     | 0.3095      | 0.2738      | -0.0358     |

Bold text indicates the miss rate difference is statistically significant.
