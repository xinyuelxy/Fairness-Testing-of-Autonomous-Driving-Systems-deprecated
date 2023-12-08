## Training Details of Open-Source Models
Our analysis utilizes two types of training datasets for the eight pedestrian detectors. General object detectors, including YOLOX, RetinaNet, Faster RCNN, and Cascade RCNN, are trained using the MS COCO training dataset (https://mmdetection.readthedocs.io/en/latest/model_zoo.html). Pedestrian-specific detectors are trained on the Citypersons datasets (https://paperswithcode.com/dataset/citypersons). Below link is the detailed specifications of these training datasets:

| Name                             | Total Images | Images with Pedestrians | Pedestrian Bounding Boxes |
|----------------------------------|--------------|-------------------------|--------------------------|
| MSCOCO Training Set              | 118,287      | 64,115                  | 262,465                  |
| CityPersons Training Set         | 2,975        | 2,975                   | 19,654                   |


To further investigate the distribution of sensitive attributes in different training datasets, we annotate person instances in these sampled images following the procedures outlined in Section 3.3.2. To ensure statistical significance while also saving manual effort, we randomly sample 723 images from the training data (382 from MS COCO and 341 from Citypersons) at a 95% confidence level with a 5% confidence interval.

Below, we present detailed information on the age, gender, and skin-tone of pedestrians instances in each dataset:

<img width="537" alt="pic1" src="https://github.com/FairnessResearch/Fairness-Testing-of-Autonomous-Driving-Systems/assets/140967709/223c6358-4b70-4d51-bf97-41ebb9dbe3e3">

<img width="585" alt="pic2" src="https://github.com/FairnessResearch/Fairness-Testing-of-Autonomous-Driving-Systems/assets/140967709/e4bfbb57-1c23-443f-88bf-9a792355b965">

<img width="543" alt="pic3" src="https://github.com/FairnessResearch/Fairness-Testing-of-Autonomous-Driving-Systems/assets/140967709/ca9e25de-8eff-4822-a86d-1fe0a94c51e9">


Our examination reveals notable imbalances in the training data distribution, where only 22.39% represented dark-skin individuals, and 9.33% were children. Furthermore, the MS COCO training dataset exhibits greater imbalance compared to the Citypersons dataset, while detectors trained on MS COCO (general object detectors) displayed more pronounced bias than those based on Citypersons (pedestrian-specific detectors). Thus, the observed biases can be attributed, in part, to imbalances in the training data. We will add this analysis to the paper.




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

Our findings are as follows:
1) Significant disparities exist in one-stage detectors: YOLOX and RetinanNet show a miss rate difference of 26.76% and 26.05%, respectively, for dark-skinned females compared to light-skinned males.
2) Despite these disparities, they are not as pronounced as the overall differences reported in Table 6, where YOLOX and RetinaNet exhibit miss rate differences of 30.7% and 28.3%, respectively, between dark-skinned and light-skinned groups.

## Bounding box size distribution for gender and skin-tone

