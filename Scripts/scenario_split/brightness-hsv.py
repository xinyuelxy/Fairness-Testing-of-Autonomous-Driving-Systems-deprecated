import os
import cv2
import shutil
import numpy as np
import pandas as pd

def getTheBright(path):
    """
    Get the brightness value
    :param path: image path
    :return: the brightness value of this image
    """
    # Load the image
    img = cv2.imread(path)

    # Convert image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Calculate mean value of V channel
    mean_v = cv2.mean(hsv)[2]

    return mean_v


def getTheYvalue():
    """
    Write the brightness value of each image to the file
    :return:
    """
    original_path = "E:/images_person/"
    files = os.listdir(original_path)
    v_values = {}
    for filename in files:
        brightness = getTheBright(original_path + filename)
        v_values[filename] = brightness
        print(f"Processed image {filename}, mean V value: {brightness:.2f}")
    print(v_values)

    # Write the dictionary to a text file
    with open("../DataSet/Fine-Grained/brightness/images/hsv-level.txt", "w") as f:
        for key, value in v_values.items():
            f.write(f"{key}: {value:.2f}\n")



def readTextGetYvalue():
    """
    Read all the value of the written scripts and classify with equal bin width
    :return:
    """
    # read dictionary from txt file
    with open('../DataSet/Fine-Grained/brightness/images/hsv-level.txt', 'r') as f:
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
    Assign the images in to 0-4 brightness levels(level1-level5) according to the results in illumination-level.txt
    :return:
    """
    class_dict = readTextGetYvalue()
    ori_path = "E:/images_person/"  #the path for all the images containing labeled person (5917images)
    dst_path = "../DataSet/Fine-Grained/brightness/images/"

    for key, value in class_dict.items():
        shutil.copy(ori_path + str(key), dst_path + str(value))
        print(str(key) + '-->' + str(value))


if __name__ == '__main__':
    getTheYvalue()
    readTextGetYvalue()
    moveTheOriImageToRightIllumination()  # move the image
