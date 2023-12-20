import os
from MLOps_project import logger
from MLOps_project.entity.config_entity import *
from sklearn.model_selection import train_test_split
import pandas as pd
import shutil

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) :
        self.config = config
    def train_test_spliting(self):
        data = pd.read_csv(self.config.label_process_data)
        train, test = train_test_split(data, random_state=48,test_size=0.25, shuffle=True)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        self.create_labels(train, activation="train/")
        self.create_labels(test, activation="test/")    
    

    def create_labels(self, data, activation: str):
        for _, row in data.iterrows():
            image_file = row['ImageID']
            class_id = "0"
            x = row['XMin']
            y = row['YMin']
            width = row['XMax'] - row['XMin']
            height = row['YMax'] - row['YMin']

            x_center = x + (width / 2)
            y_center = y + (height / 2)
            
            labels_dir = os.path.join(self.config.root_dir, "labels")
            self.create_folder(labels_dir)
            activation_dir = os.path.join(labels_dir, activation)
            self.create_folder(activation_dir)

            annotation_file = os.path.join(activation_dir, image_file + '.txt')
            with open(annotation_file, 'w') as ann_file:
                ann_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
        
        logger.info(f"Created label folders finished")

    def image_splitting(self):
        train_data = pd.read_csv(os.path.join(self.config.root_dir, "train.csv"))
        test_data = pd.read_csv(os.path.join(self.config.root_dir, "test.csv"))

        self.create_folder(self.config.image_train_data)
        self.create_folder(self.config.image_test_data)

        self.copy_images(train_data, self.config.image_train_data)
        self.copy_images(test_data, self.config.image_test_data)

        train_image_count = self.count_img_in_dir(self.config.image_train_data)
        logger.info(f"number image in train image directory: {train_image_count}")
        test_image_count = self.count_img_in_dir(self.config.image_test_data)
        logger.info(f"number image in train image directory: {test_image_count}")

    def create_folder(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            logger.info(f"Created folder: {folder_path}")

    def count_img_in_dir(self, directory):
        count = sum([len(files) for _, _, files in os.walk(directory)])
        return count
   
    def copy_images(self, data, target_folder):
        source_folder = self.config.image_root_data
        list_data = data["ImageID"].apply(lambda x: x + ".jpg").tolist()

        for file in os.listdir(source_folder):
            if file.endswith(".jpg") and file in list_data:
                source_path = os.path.join(source_folder, file)
                target_path = os.path.join(target_folder, file)
                shutil.copy(source_path, target_path)   
    