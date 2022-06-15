import sys
import os
try:
    from tqdm import tqdm
    module_found = True
except:
    module_found = False

def label_txt(dataset):
    if dataset == "train":
        folder_official = "D:/Data/2D/database/yolov5/coco/labels_default/" # change the path according to your original dataset such as coco2017
        folder_custom = "D:/Data/2D/database/yolov5/coco/labels/" # change the path according to the dataset you want to generate
        folder_type = "train2017" #
    if dataset == "val":
        folder_official = "D:/Data/2D/database/yolov5/coco/labels_default/" # change the path according to your original dataset such as coco2017
        folder_custom = "D:/Data/2D/database/yolov5/coco/labels/" # change the path according to the dataset you want to generate
        folder_type = "val2017" #

    files = list(os.listdir(folder_official+folder_type))
    print(files)
    cnt_obj = 0
    all_files = len(files)
    cnt_files = 0

    if module_found:
        process_bar = tqdm(total=all_files)
        process_bar.set_description('Processing:')
    for file in files:
        custom_label = [] 
        open_txt = False
        if module_found:
            process_bar.update(1)
        else:
            cnt_files += 1
            progress = str("%.2f" % (cnt_files/all_files*100))
            sys.stdout.write('\r'+ f"Progress:{progress}%")

        with open(os.path.join(folder_official+folder_type, file), 'r') as f:
            strs = [x.split() for x in f.read().strip().splitlines()]
            for single_line in strs:
                if single_line[0] == '0': # change "0" to the label you want; modifying the codes to add labels accordingly; "0" is the label of "person" in coco2017
                    custom_label.append(single_line)
                    cnt_obj += 1
                    open_txt = True
            f.close()
        if open_txt == True:
            with open(os.path.join(folder_custom+folder_type, file), 'w') as fp:
                for line in custom_label:
                    newline = " ".join(line) + "\n"
                    fp.writelines(newline)
                fp.close()
            
    print(f'\nnumber of target:{cnt_obj}')

label_txt("train")
label_txt("val")

def whole_txt(dataset):
    if dataset == "train":
        folder = "train2017"
        files = list(os.listdir(folder))
        with open('../train2017_person.txt', 'w') as ftrain:
            for file in files:
                line = './images/train2017/' + file.replace("txt", "jpg") + '\n'
                ftrain.writelines(line)
            ftrain.close()
    
    if dataset == "val":
        folder = "val2017"
        files = list(os.listdir(folder))
        with open('../val2017_person.txt', 'w') as fval:
            for file in files:
                line = './images/val2017/' + file.replace("txt", "jpg") + '\n'
                fval.writelines(line)
            fval.close()

whole_txt("train")
whole_txt("val")

import shutil
def create_img_folder():
    img_folder = "D:/Data/2D/database/yolov5/coco/images/train2017/"
    new_img_folder = "D:/Data/2D/database/yolov5/coco_person/images/train2017/"
    folder = "train2017"
    files = list(os.listdir(folder))
    all_files = len(files)
    if not os.path.exists(new_img_folder):
        os.makedirs(new_img_folder)
    if module_found:
        process_bar = tqdm(total=all_files)
        process_bar.set_description('Processing:')
    for file in files:
        process_bar.update(1)
        img = img_folder + file.replace("txt", "jpg")
        shutil.copy(img, new_img_folder)

# create_img_folder()

'''
Download txt label of COCO
https://github.com/ultralytics/yolov5/releases/download/v1.0/coco2017labels.zip
'''
