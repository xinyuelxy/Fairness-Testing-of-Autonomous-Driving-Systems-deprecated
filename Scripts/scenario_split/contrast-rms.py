import os
import cv2
import shutil
import numpy as np
import pandas as pd



def getTheContrast(path):
    """
    求取图像的亮度值
    :param path: 输入图像路径
    :return: 返回该图像rms contrast
    """

    # Load the image in grayscale mode
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Calculate the mean intensity of the image
    mean_intensity = cv2.mean(img)[0]

    # Calculate the RMS contrast
    rms_contrast = np.sqrt(np.mean((img - mean_intensity) ** 2))

    return rms_contrast

def getTheYvalue():
    """
    获得文件夹下所有图像的Y值
    :return:
    """
    original_path = "E:/images_person/"
    files = os.listdir(original_path)
    v_values = {}
    for filename in files:
        brightness = getTheContrast(original_path + filename)
        v_values[filename] = brightness
        print(f"Processed image {filename}, RMS_Contrast: {brightness:.2f}")
    print(v_values)

    # Write the dictionary to a text file
    with open("../DataSet/Fine-Grained/contrast/contrast-level.txt", "w") as f:
        for key, value in v_values.items():
            f.write(f"{key}: {value:.2f}\n")


def readTextGetYvalue():
    """
    得到txt文件中的所有Y值
    :return:
    """
    # read dictionary from txt file
    with open('../DataSet/Fine-Grained/contrast/images/contrast-level.txt', 'r') as f:
        d = dict(line.strip().split(': ') for line in f)

    # Extract values from dictionary
    contrast_value = np.array(list(d.values()), dtype=float)

    #define the num of classes
    num_classes = 5
    class_labels = range(num_classes)
    class_assignments, bin_edges = pd.cut(contrast_value, num_classes, labels=class_labels, retbins=True)

    # Print the class ranges
    for i in range(num_classes):
        print(f'Class {i}: {bin_edges[i]} to {bin_edges[i + 1]}')
    bin_width = bin_edges[1] - bin_edges[0]
    print(f'The bin width is {bin_width}.')

    # Create a new dictionary that maps keys to their corresponding classes
    class_dict = {key: class_assignments[i] for i, key in enumerate(d.keys())}

    # Print the class assignments for each key in the dictionary
    for key, value in class_dict.items():
        print(f'{key}: {value}')

    return class_dict

def moveTheOriImageToRightIllumination():
    """
    根据illumination-level.txt中的结果将illumination_test_images中的图像分配到0-4种亮度等级中
    :return:
    """
    class_dict = readTextGetYvalue()
    ori_path = "E:/images_person/"
    dst_path = "../DataSet/Fine-Grained/contrast/images/"

    for key, value in class_dict.items():
        shutil.copy(ori_path + str(key), dst_path + str(value))
        print(str(key) + '-->' + str(value))


if __name__ == '__main__':
    #getTheYvalue()
    readTextGetYvalue()
    moveTheOriImageToRightIllumination()  # 移动图像