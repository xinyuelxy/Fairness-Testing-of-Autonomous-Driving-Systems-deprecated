# Unveiling the Blind Spots: A Critical Examination of Fairness in Autonomous Driving Systems    

Welcome to the online appendix for the paper entitled "Unveiling the Blind Spots: A Critical Examination of Fairness in Autonomous Driving Systems". Here, we provide supplementary materials including raw results,  datasets and sensitive attributes labels, Python code for the analysis process, and scripts to replicate our experiments.

## Datasets

In this directory, we present the datasets used in our experiments. The "Datasets" directory is organized into two aspects: the four testing datasets we used in RQ1 (overall) and the partitioned datasets in each scenario (partitioned) in RQ2. The structure of the directory is as follows (the numbers in parentheses represent the number of images in each folder):

```
Datasets
|
|-- overall
|   |-- citypersons(#1,525)
|   |-- ecp_day (#2,427)
|   |-- ecp_night (#2,126)
|   |-- bdd100k (#2,233)
|
|-- partitioned
    |-- brightness
    |   |-- day and night
    |		|-- day(#4,400), night(#1,517)
    |   |-- five brightness levels
    |		|-- level1(#189), level2(#1,128), level3(#3,166), level4(#1,318), level5(#116)
    |
    |-- contrast
    |   |-- five contrast levels
    |    	|-- level1(#246), level2(#1,523), level3(#2,383), level4(#1,667), level5(#98)
    |
    |-- weather
        |-- rainy(#277)
        |-- non-rainy(#3800)
```


All the datasets can be downloaded from the provided link with aforementioned structure: 

> baidunetdisk: 

The four benchmark testing datasets used in our experiments, as described in <u>Section 3.3.1</u>. The datasets are detailed in "*Table 2: Benchmark Datasets*" in our academic paper, providing information on the number of images and the time of capture for each dataset. 

In addition,  we also provide the partitioned datasets from the scenario labeling discussed in <u>Section 3.3.3</u>. The scripts employed for partitioning these datasets can be located in the "Scripts" directory.  RQ2 focuses on real-world key scenarios, each having its respective sub-folder: brightness, contrast, and weather. Detailed information is presented in "*Table 5: Number of images in different brightness levels, contrast levels, and weather conditions*."

## Labels

In the "Labels" directory, we provide the labels used in our experiments. This folder is divided into two main parts. The first part includes the labels for RQ1: Overall Fairness ("RQ1_overall" sub-directory), containing ground-truth labels for the four testing datasets. These labels are organized based on four testing datasets. The second part encompasses the labels for RQ2: Fairness in Different Scenarios ("RQ2_partitioned" sub-directory).  These labels are categorized based on fine-grained scenarios we discussed.

### 1. RQ1 Overall Fairness (RQ1_overall)

The "Labels" folder is structured as follows. The "GT" subdirectory contains ground-truth labels for each of the four testing datasets: "bdd100k," "citypersons," "ecp_day," and "ecp_night." Within this directory, the labels are further categorized based on their attributes and stored in corresponding sub-folders.

Similarly, the "DT" subdirectory is also organized according to the four testing datasets: "bdd100k," "citypersons," "ecp_day," and "ecp_night." It contains predicted labels from eight pedestrian detectors for each dataset. The predicted labels are stored in sub-folders named after the respective detectors, such as "yolox," "retinanet," "faster rcnn," "cascade rcnn," "alfnet," "prnet," "csp," and "mgan."

```
RQ1_overall
|
|-- GT
|   |-- bdd100k
|   |   |-- gender, age, skin
|   |-- citypersons
|   |   |-- gender, age
|   |-- ecp_day
|   |   |-- gender, age
|   |-- ecp_night
|       |-- gender, age
|-- DT
    |-- bdd100k
    |   |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
    |-- citypersons
    |   |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
    |-- ecp_day
    |   |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
    |-- ecp_night
        |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
```


The GT and DT format is explained as follows:

**(1) GT  (Ground-Truth Labels)**

The "GT" directory contains ground-truth labels for each dataset, as detailed in "*Table 4: Number of labeled pedestrian instances per dataset.*" in our academic paper. For the "BDD100k" dataset, we provide formulated  skin tone, age and gender labels on all four testing datasets. 

Each image's ground truth label is stored in a separate TXT file within the corresponding attribute's folder. For example, in the "cp" dataset, the gender label for the image `berlin_000003_000019_leftImg8bit.png` can be found in the file `berlin_000003_000019_leftImg8bit.txt` within the `./Labels/RQ1_overall/GT/citypersons/gender/` directory. Each TXT file can contain labels for multiple individuals present in the image.

The manual labeling process was performed using LabelImg, with the original format being in YOLO format. We have formulated each label's format in a more precise way, and the code for this formulation can be found in the "Script" directory. After that, the formulated GT label for each person is represented using a *five-digit format*, taking gender as an example:

`gender X_min Y_min X_max Y_max`

Here, "gender" denotes the gender classification, where 0 represents male and 1 represents female. For other attributes, such as skin tone (0 for light-skin, 1 for dark-skin), and age (0 for adult, 1 for child), similar conventions apply.

The values X_min, Y_min, X_max, and Y_max are used to describe the *bounding box* of the target object:

- `X_min` and `Y_min`: The coordinates of the **top-left corner** of the bounding box.

- `X_max` and `Y_max`: The coordinates of the **bottom-right corner** of the bounding box.

Our bounding boxes start at the point (`X_min`, `Y_min`) and end at the point (`X_max`, `Y_max`). Let's consider one of the sample images as an example:

![image-20230727173236222](E:\Relased Code\README.assets\image-20230727173236222.png)

The final label for the middle person is: 

`0 (male) 787 257 (top-left corner) 1068 768 (bottom-right corner)`

**(2) DT (Detected Labels/Predicted Labels)**

The detected labels refer to the prediction information made by the 8 pedestrian detectors on the locations of "predicted person" in the four testing datasets. For each image's inference result, there is a corresponding TXT file. Within each TXT file, the organization format for the prediction result of a person is represented in a five-digit format, as follows:

`confidence_score X_min Y_min X_max Y_max`

Confidence_score represents the probability assigned by the pedestrian detector to the prediction, indicating the level of certainty that the detector has in its prediction. To ensure the reliability of the predictions, we retain only those predictions with a confidence score higher than 50%. 

`X_min`, `Y_min`, `X_max`, and `Y_max` carry the same meaning as in the GT. They denote the coordinates of the bounding box enclosing the predicted person, where `X_min` and `Y_min` correspond to the top-left corner, and `X_max` and `Y_max` correspond to the bottom-right corner of the bounding box.

### 2. RQ2 Fairness in Different Scenarios (RQ2_partitioned)

In this section, we present the structured label information for RQ2 - Fairness in Different Scenarios ("RQ2_partitioned" directory). The labels has been categorized based on the classified dataset in "Dataset" part explained in the previous dataset introduction. The directory structure is as follows:

```
RQ2_partitioned
|
|-- brightness
|   |-- day_night
|       |-- GT
|        	|-- day,night
|        	 	|-- gender, age, skin
|       |-- DT
|        	|-- day,night
|        	 	|-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
|   |-- five_brightness_levels
|       |-- GT
|        	|-- level1,level2, level3, level4, level5
|        	 	|-- gender, age, skin
|       |-- DT
|        	|-- level1,level2, level3, level4, level5
|        	 	|-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
|       |-- hsv-info
|        	|-- hsv-level.txt
|-- contrast
|   |-- five_contrast_levels
|       |-- GT
|        	|-- level1,level2, level3, level4, level5
|        	 	|-- gender, age, skin
|       |-- DT
|       	|-- level1,level2, level3, level4, level5
|       	 	|-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
|       |-- rms-info
|       	|-- contrast-level.txt
|-- weather
    |-- GT
        |-- rainy, non-rainy
         	|-- gender, age, skin
    |-- DT
        |-- rainy, non-rainy
         	|-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
```

Within each scenario (brightness, contrast, and weather), there are corresponding "GT" and "DT" directories. The structure of the "GT" directories' meaning is identical to that in RQ1_overall, containing ground-truth labels for each attribute, such as "gender," "age," and "skin." The "DT" directories also store the predicted labels from the eight pedestrian detectors.  At the same time,  as mentioned in Section 3.3.3, we provide the brightness and contrast values for all images containing labeled pedestrians with a total of 5,917 images. These values can be found in the `hsv-level.txt` and `contrast-level.txt`.

## Pedestrian Detection Models

In this section, we provide a detailed description of the experimental settings for eight pedestrian detection models as discussed in <u>Section 3.2</u> with "*Table 1: Representative pedestrian detectors.*". The experiments configuration are implemented with their corresponding open-source framework.

- MMDetection (YOLOX, RetinaNet, Faster RCNN, and Cascade RCNN): [Benchmark and Model Zoo — MMDetection 3.1.0 documentation](https://mmdetection.readthedocs.io/en/stable/model_zoo.html)

- Pedestron (CSP, MGAN): [GitHub - hasanirtiza/Pedestron: [Pedestron\] Generalizable Pedestrian Detection: The Elephant In The Room. @ CVPR2021](https://github.com/hasanirtiza/Pedestron)
- ALFNet: [GitHub - liuwei16/ALFNet: Code for 'Learning Efficient Single-stage Pedestrian Detectors by Asymptotic Localization Fitting' in ECCV2018](https://github.com/liuwei16/ALFNet)
- PRNet: [GitHub - sxlpris/PRNet: Code for "Progressive Refinement Network for Occluded Pedestrian Detection" in ECCV2020.](https://github.com/sxlpris/PRNet)

In particular, all experiments were performed on a system equipped with 64GB RAM, 2.5GHz Intel Xeon (R) v3 Dual CPUs, and one NVIDIA GeForce RTX 2080 Ti GPU. YOLOX, RetinaNet, Faster RCNN, and Cascade RCNN were implemented using PyTorch 1.8.1 and Python 3.7.10 on Ubuntu 18.04 LTS, following the MMdetection configuration. CSP and MGAN utilized PyTorch 1.10.0 and Python 3.8.10 on Ubuntu 18.04 LTS, adhering to the Pedestron configuration. Finally, ALFNet and PRNet  were implemented using Keras 2.0.6, Tensorflow 1.4.0, and Python 2.7.18 on Ubuntu 16.04 LTS following the instruction and configuration in the public framework they released.

For accessibility, all the public models we used can be downloaded from the following link：

> baidunetdisk: https://pan.baidu.com/s/1ZuexG8A972y8ddbwy7n2qw ; code：tvgf

The predicted results from each model can be found in the "DT" directory as previously mentioned.

## Scripts
In this section, we provide the computational code for <u>Section 4</u> of the paper.  The "evaluation" folder contains the essential code for generating Table 6, Figure 1, Figure 2, Figure 3, Table 7, Figure 4, Figure 5, and Table 8. Additionally, it includes a demonstration example for computing evaluation metrics and performing statistical analysis. The "scenario_split" folder offers the code used in Section 3.3.3 of the paper, specifically for partitioning datasets based on five brightness and contrast levels.  Moreover, the "label_process" folder contains code that may be helpful to future researchers when processing and handling labels in their experiments.

For obtaining our results, you will only need to use the organized "Labels" folder and some of the scripts provided in these directories. The "evaluation" folder will be instrumental in generating the evaluation results and figures, while the "scenario_split" folder will help in investigating fairness in different scenarios. Finally, the "label_process" folder will assist in the label processing required during the experiments.

### 2. Evaluation










### 3. Scenario Split



### 4. Label Process



### 



## Results


