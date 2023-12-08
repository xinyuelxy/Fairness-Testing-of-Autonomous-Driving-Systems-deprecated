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

Furthermore, we have compared bounding box size distribution for men and women, and for dark-skin and light-skin individuals. Our findings reveal a comparable distribution in bounding box size between light-skin and dark-skin individuals. Likewise, women and men exhibit a similar distribution in bounding box size. This suggests that biases observed in gender and skin tone may not be attributed to differences in bounding box size. Detailed results have been included in our repository.

<img width="930" alt="distribution" src="https://github.com/FairnessResearch/Fairness-Testing-of-Autonomous-Driving-Systems/assets/140967709/5cb9a869-dcda-4a92-8f9b-665f0f7fd51b">


## Average miss rates for children and adults in each dataset (supplementary material for Fig 1)

<img width="930" alt="distribution" src="https://github.com/FairnessResearch/Fairness-Testing-of-Autonomous-Driving-Systems/assets/140967709/115aecea-52de-436e-8742-d2122d28dfb9">


Bold text indicates the miss rate difference is statistically significant.


## Accuracy on age groups broken down by bounding box size

We further categorize bounding box sizes into three levels (1-3), where larger sizes are indicated by higher levels. Our analysis reveals a trend where the disparity in detection accuracy between adults and children increases as bounding box sizes decrease. Specifically, Level 3 has an 8.99% gap (Adults: 23.36%, Children: 32.35%), Level 2 shows a 10.15% difference (Adults: 23.58%, Children: 33.72%), and Level 1 demonstrates a 23.95% disparity (Adults: 31.89%, Children: 55.85%). These findings suggest that smaller bounding box sizes significantly contribute to the bias in detection accuracy.

<table border="1">
  <tr>
    <th></th>
    <th colspan="3" style="background-color: #FFEEBA;">Small Bounding Boxes Size (Level 1)</th>
    <th colspan="3" style="background-color: #FFEEBA;">Middle Bounding Boxes Size (Level 2)</th>
    <th colspan="3" style="background-color: #FFEEBA;">Large Bounding Boxes Size (Level 3)</th>
  </tr>
  <tr>
    <td>Detectors</td>
    <td>MR_adult</td>
    <td>MR_child</td>
    <td>EOD</td>
    <td>MR_adult</td>
    <td>MR_child</td>
    <td>EOD</td>
    <td>MR_adult</td>
    <td>MR_child</td>
    <td>EOD</td>
  </tr>
  <tr>
    <td>yolox</td>
    <td>51.33%</td>
    <td>72.06%</td>
    <td style="background-color: grey;"><strong>-20.72%</strong></td>
    <td>21.55%</td>
    <td>32.89%</td>
    <td style="background-color: grey;"><strong>-11.34%</strong></td>
    <td>9.23%</td>
    <td>18.63%</td>
    <td style="background-color: grey;"><strong>-9.39%</strong></td>
  </tr>
  <tr>
    <td>retinanet</td>
    <td>36.51%</td>
    <td>65.88%</td>
    <td style="background-color: grey;"><strong>-29.37%</strong></td>
    <td>17.24%</td>
    <td>30.87%</td>
    <td style="background-color: grey;"><strong>-13.64%</strong></td>
    <td>9.93%</td>
    <td>18.63%</td>
    <td style="background-color: grey;"><strong>-8.70%</strong></td>
  </tr>
  <tr>
    <td>faster_rcnn</td>
    <td>12.69%</td>
    <td>38.53%</td>
    <td style="background-color: grey;"><strong>-25.83%</strong></td>
    <td>5.61%</td>
    <td>16.78%</td>
    <td style="background-color: grey;"><strong>-11.17%</strong></td>
    <td>2.79%</td>
    <td>10.78%</td>
    <td style="background-color: grey;"><strong>-7.99%</strong></td>
  </tr>
  <tr>
    <td>cascade_rcnn</td>
    <td>14.43%</td>
    <td>42.35%</td>
    <td style="background-color: grey;"><strong>-27.93%</strong></td>
    <td>6.35%</td>
    <td>17.45%</td>
    <td style="background-color: grey;"><strong>-11.10%</strong></td>
    <td>3.24%</td>
    <td>11.76%</td>
    <td style="background-color: grey;"><strong>-8.53%</strong></td>
  </tr>
  <tr>
    <td>csp</td>
    <td>29.22%</td>
    <td>50.88%</td>
    <td style="background-color: grey;"><strong>-21.66%</strong></td>
    <td>34.12%</td>
    <td>44.30%</td>
    <td style="background-color: grey;"><strong>-10.18%</strong></td>
    <td>49.19%</td>
    <td>57.84%</td>
    <td style="background-color: grey;"><strong>-8.65%</strong></td>
  </tr>
  <tr>
    <td>mgan</td>
    <td>32.16%</td>
    <td>50.00%</td>
    <td style="background-color: grey;"><strong>-17.84%</strong></td>
    <td>32.02%</td>
    <td>38.26%</td>
    <td style="background-color: grey;"><strong>-6.23%</strong></td>
    <td>36.41%</td>
    <td>47.06%</td>
    <td style="background-color: grey;"><strong>-10.65%</strong></td>
  </tr>
  <tr>
    <td>alfnet</td>
    <td>39.93%</td>
    <td>63.24%</td>
  <td style="background-color: grey;"><strong>-23.31%</strong></td>
  <td>34.15%</td>
  <td>40.94%</td>
  <td style="background-color: grey;"><strong>-6.79%</strong></td>
  <td>35.89%</td>
  <td>39.22%</td>
  <td style="background-color: grey;"><strong>-3.32%</strong></td>
  </tr>
  <tr>
  <td>prnet</td>
  <td>38.88%</td>
  <td>63.82%</td>
  <td style="background-color: grey;"><strong>-24.95%</strong></td>
  <td>37.60%</td>
  <td>48.32%</td>
  <td style="background-color: grey;"><strong>-10.72%</strong></td>
  <td>40.21%</td>
  <td>54.90%</td>
  <td style="background-color: grey;"><strong>-14.69%</strong></td>
  </tr>
  <tr>
  <td>overall</td>
  <td>31.89%</td>
  <td>55.85%</td>
  <td style="background-color: grey;"><strong>-23.95%</strong></td>
  <td>23.58%</td>
  <td>33.72%</td>
  <td style="background-color: grey;"><strong>-10.15%</strong></td>
  <td>23.36%</td>
  <td>32.35%</td>
  <td style="background-color: grey;"><strong>-8.99%</strong></td>
  </tr>
</table>



Bold text indicates the miss rate difference is statistically significant. 

## Preliminary study on contrast + image editing method 

As Table 6 suggests, YOLOX and RetinaNet show the greatest bias among all detectors we study. Therefore, due to the time limit, we use the two detectors for experiments. We randomly select 1294 images from our test data, ensuring a 95% confidence level with a 5% confidence interval. We use the OpenCV tool to increase the contrast of these images (adjusting alpha from 1 to 1.4). We find that contrast enhancement can significantly reduce bias. Particularly, the undetected proportions gap in YOLOX and RetinaNet between light-skinned and dark-skinned pedestrians dropped from 27.33% and 24.92% to 2.84% and 5.66%, respectively.

| Setting                       | Detectors | MR_LS  | MR_DS   | EOD       |
|-------------------------------|-----------|--------|---------|-----------|
| Contrast-Original (alpha = 1) | yolox     | 9.12%  | 36.45%  | **-27.33%** |
|                               | retinanet | 11.53% | 36.45%  | **-24.92%** |
| Contrast-1.4 (alpha = 1.4)    | yolox     | 9.38%  | 6.54%   | **2.84%**   |
|                               | retinanet | 13.14% | 7.48%   | **5.66%**   |


Bold text indicates the miss rate difference is statistically significant. 








