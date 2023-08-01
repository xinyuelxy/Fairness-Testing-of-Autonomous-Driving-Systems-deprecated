# Unveiling the Blind Spots: A Critical Examination of Fairness in Autonomous Driving Systems

Welcome to the online appendix for the paper entitled "Unveiling the Blind Spots: A Critical Examination of Fairness in Autonomous Driving Systems". Here, we provide supplementary materials including raw results, Python code for the analysis process, and scripts to replicate our experiments.

## Datasets and Labels

In this directory, we present the datasets and labels used in our experiments.

### 1. Datasets

The "Datasets" directory is structured as follows:

```
Datasets
|
|-- Four Benchmark Testing Datasets
|   |-- bdd100k
|   |-- cp
|   |-- ecp_day
|   |-- ecp_night
|
|-- The partitioned dataset in each scenario
    |-- brightness
    |   |-- day and night
    |   |-- five brightness levels
    |
    |-- contrast
    |   |-- five contrast levels
    |
    |-- weather
        |-- rainy-weather
        |-- dry-weather
```



**(1) Four Benchmark Testing Datasets**

Our experiments utilize these four benchmark testing datasets, as described in Table 2 (Benchmark datasets for fairness testing) in our academic paper. The table provides details on each dataset's size and time of capture.

|            Datasets            |     Size     |    Time    |
| :----------------------------: | :----------: | :--------: |
|      CityPersons (**cp**)      | 1,525 images |    day     |
|   EuroCity Day (**ecp_day**)   | 2,427 images |    day     |
|     BDD100K (**bdd100K**)      | 2,233 images | day, night |
| EuroCity Night (**ecp_night**) | 2,126 images |   night    |

All the testing datasets can be downloaded from the provided link:  

**(2) The partitioned dataset in each scenario**

In addition, we also offer the partitioned datasets used in RQ2. The scripts used for partitioning these datasets can be found in the "Scripts" directory. RQ2 focuses on real-world key scenarios, each with its respective sub-folder: brightness, contrast and weather.

These partitioned datasets can be downloaded here:

### 2. Labels

The "GT" subdirectory contains ground-truth labels for each of the four testing datasets. Within this directory, each dataset's labels are categorized based on their attributes and stored in corresponding sub-folders. Similarly, the "DT" subdirectory is also organized according to the four testing datasets, and it contains predicted labels from eight pedestrian detectors for each dataset. To summarize, the structure of the "Labels" folder is as follows:

```
Labels
|
|-- GT
|   |-- bdd100k
|   |   |-- skin, gender, age
|   |
|   |-- cp
|   |   |-- gender, age
|   |
|   |-- ecp_day
|   |   |-- gender, age
|   |
|   |-- ecp_night
|       |-- gender, age
|
|-- DT
    |-- bdd100k
    |   |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
    |
    |-- cp
    |   |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
    |
    |-- ecp_day
    |   |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan
    |
    |-- ecp_night
        |-- yolox, retinanet, faster rcnn, cascade rcnn, alfnet, prnet, csp, mgan

```



**(1) GT  (Ground-Truth Labels)**

The "GT" directory contains ground-truth labels for each dataset, as detailed in Table 4 (Count of labeled instances on each dataset) in our academic paper. For the "bdd100k" dataset, we provide skin-tone labels formulated based on the research conducted by Wilson et al. [Link to Wilson et al.], along with manually labeled  information for age and gender on all four testing datasets. 

Each image's ground truth label is stored in a separate TXT file within the corresponding attribute's folder. For example, in the "cp" dataset, the gender label for the image `berlin_000003_000019_leftImg8bit.png` can be found in the file `berlin_000003_000019_leftImg8bit.txt` within the `Datasets and Labels/Labels/GT/cp/gender/` directory. Each TXT file can contain labels for multiple individuals present in the image.

The manual labeling process was performed using LabelImg, with the original format being in YOLO format. We have formulated each label's format in a more precise way, and the code for this formulation can be found in the "Script" directory. The formulated GT label for each person is represented using a *five-digit format*, taking gender as an example:

`gender X_min Y_min X_max Y_max`

Here, "gender" denotes the gender classification, where 0 represents male and 1 represents female. For other attributes, such as skin-tone (0 for LS, 1 for DS), and age (0 for adult, 1 for child), similar conventions apply.

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

## Pedestrian Detection Models

In this section, we describe the experimental settings on eight pedestrian detection in detail. The experiments are implemented with their corresponding open-source framework.

- MMDetection (YOLOX, RetinaNet, Faster RCNN, and Cascade RCNN): [Benchmark and Model Zoo — MMDetection 3.1.0 documentation](https://mmdetection.readthedocs.io/en/stable/model_zoo.html)

- Pedestron (CSP, MGAN): [GitHub - hasanirtiza/Pedestron: [Pedestron\] Generalizable Pedestrian Detection: The Elephant In The Room. @ CVPR2021](https://github.com/hasanirtiza/Pedestron)
- ALFNet: [GitHub - liuwei16/ALFNet: Code for 'Learning Efficient Single-stage Pedestrian Detectors by Asymptotic Localization Fitting' in ECCV2018](https://github.com/liuwei16/ALFNet)
- PRNet: [GitHub - sxlpris/PRNet: Code for "Progressive Refinement Network for Occluded Pedestrian Detection" in ECCV2020.](https://github.com/sxlpris/PRNet)

In particular, all experiments were performed on a system equipped with 64GB RAM, 2.5GHz Intel Xeon (R) v3 Dual CPUs, and one NVIDIA GeForce RTX 2080 Ti GPU. YOLOX, RetinaNet, Faster RCNN, and Cascade RCNN were implemented using PyTorch 1.8.1 and Python 3.7.10 on Ubuntu 18.04 LTS, following the MMdetection configuration. CSP and MGAN utilized PyTorch 1.10.0 and Python 3.8.10 on Ubuntu 18.04 LTS, adhering to the Pedestron configuration. Finally, ALFNet and PRNet  were implemented using Keras 2.0.6, Tensorflow 1.4.0, and Python 2.7.18 on Ubuntu 16.04 LTS following the instruction and configuration in the public framework they released.

For accessibility, all the public models we used can be downloaded from the following link:

Furthermore, the detected results for each model can be found in the "DT" directory as previously mentioned.

## Scripts
This section provides step-by-step instructions on how to set up the required packages and libraries for running the code and reproducing our results.

### 1. Python Configuration
For our experiments, we used Python 3.7. Furthermore, we require the following Python packages:

```
pip install sklearn
pip install numpy
pip install cv2
```


## Example



## Results

