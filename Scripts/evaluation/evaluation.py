import glob
import os
from statsmodels.stats.proportion import proportions_ztest
import argparse

# Parameters setting in section
PRED_THRES = 0.5
IOU_THRES = 0.5
ATTR_MAPPING = {
    'age': {0: 'Adults', 1: 'Children'},
    'gender': {0: 'Male', 1: 'Female'},
    'skin': {0: 'Light-Skin', 1: 'Dark-Skin'}
}
DT_TYPES = ['yolox', 'retinanet', 'faster_rcnn', 'cascade_rcnn', 'alfnet', 'csp', 'mgan', 'prnet']  # List of DT types

# Calculate IoU
def cal_iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
    if interArea == 0:
        return 0

    boxAArea = abs((boxA[2] - boxA[0]) * (boxA[3] - boxA[1]))
    boxBArea = abs((boxB[2] - boxB[0]) * (boxB[3] - boxB[1]))

    iou = interArea / float(boxAArea + boxBArea - interArea)

    return iou

# Read the data from a file
def read_file(file_path):
    with open(file_path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

# Main detection function
def detect(attribute, gt_path, dt_path):
    GT_files_list = glob.glob(gt_path + '\\*.txt')
    overall_results = {}

    for dt_type in DT_TYPES:  # Iterate through all the detection types
        success_count = [0, 0]
        failure_count = [0, 0]

        dt_type_path = os.path.join(dt_path, dt_type)

        for GT_txt_file in GT_files_list:
            file_id = GT_txt_file.split(".txt", 1)[0]
            file_name = os.path.basename(os.path.normpath(file_id))
            DT_filepath = dt_type_path + '\\' + file_name + '.txt'

            if not os.path.exists(DT_filepath):
                GT_lines = read_file(GT_txt_file)
                for GT_line in GT_lines:
                    category = int(GT_line[0])
                    failure_count[category] += 1
            else:
                GT_lines = read_file(GT_txt_file)
                DT_lines = read_file(DT_filepath)

                for GT_line in GT_lines:
                    items = [float(item) for item in GT_line.split(' ')]
                    category, bb_GT = int(items[0]), items[1:]

                    iou_max = 0
                    for DT_line in DT_lines:
                        items = [float(item) for item in DT_line.split(' ')]
                        conf, bb_DT = items[0], items[1:]
                        iou = cal_iou(bb_GT, bb_DT)
                        iou_max = max(iou, iou_max)

                    if iou_max > IOU_THRES and conf >= PRED_THRES:
                        success_count[category] += 1
                    else:
                        failure_count[category] += 1

        overall_results[dt_type] = (success_count, failure_count)

    return overall_results, ATTR_MAPPING[attribute]

def main():
    parser = argparse.ArgumentParser(description="Script for evaluating attributes")
    parser.add_argument('--attribute', type=str, required=True,
                        choices=['age', 'gender', 'skin'],
                        help='Attribute for evaluation: age, gender or skin')
    parser.add_argument('--gt_path', type=str, required=True,
                        help='Path to ground truth files')
    parser.add_argument('--dt_path', type=str, required=True,
                        help='Path to prediction files')

    args = parser.parse_args()

    overall_results, attribute_mapping = detect(args.attribute, args.gt_path, args.dt_path)

    print("\n========== Evaluation Results ==========\n")
    print(f"Current Testing Attribute: {args.attribute.capitalize()}")

    for dt_type, (success_count, failure_count) in overall_results.items():
        total_count = [success_count[i] + failure_count[i] for i in range(2)]
        total = sum(total_count)
        recall = [success_count[i] / total_count[i] for i in range(2)]
        EOD = recall[1] - recall[0]

        print(f"\n========== DT Type: {dt_type} ==========\n")
        print(f"Total Samples: \t{total}")

        for i in range(2):
            print(f"\n{attribute_mapping[i]} Results:")
            print(f"\tTotal: {total_count[i]}")
            print(f"\tSuccessful Detections: {success_count[i]}")
            print(f"\tMR: {1-recall[i]:.4f}")

        print(f"\nEqual Opportunity Difference (EOD):\n\t{EOD:.4f}")

        z_score, p_value = proportions_ztest([success_count[0], success_count[1]], [total_count[0], total_count[1]],
                                             alternative='two-sided')

        print(f"\nTwo Proportions Z-test (P-value):\n\t{p_value}")

if __name__ == "__main__":
    main()

#trial scripts in terminal: python .\evaluation\evaluation.py --attribute age --gt_path '..\Labels\RQ1_Overall\GT\citypersons\age' --dt_path '..\Labels\RQ1_Overall\DT\citypersons'
