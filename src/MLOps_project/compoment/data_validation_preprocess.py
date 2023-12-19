import os
import cv2
import pandas as pd
from MLOps_project import logger
from MLOps_project.utils.common import get_size
from MLOps_project.entity.config_entity import * 
from PIL import Image

class DataValidation_Preprocess:
    def __init__(self, config: DataValidation_PreprocessConfig):
        self.config = config
        self.data = None
    
    def open_csv(self):
        self.data = pd.read_csv(self.config.label_root_data)
        return self.data
    def validate_columns(self)-> bool:
        try:
            all_cols = list(self.data.columns)

            validation_status = None
            choose_schema = self.config.choose_schema.keys()

            for col in all_cols:
                if col not in choose_schema:
                    validation_status = 0
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Validation status of choose{col} for schema: {validation_status}\n")
                else:
                    validation_status = 1
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"VaValidation status of choose{col} for schema: {validation_status}\n")
            return validation_status, self.data
        
        except Exception as e:
            raise e
    def drop_duplicate(self):
        try:
            self.data = self.data.drop_duplicates()
            self.data = self.data.dropna()
            output_folder = os.path.dirname(self.config.label_process_data)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            self.data.to_csv(self.config.label_process_data, index=False)
        except Exception as e:
            raise e
    def process_image(self):
        try:
            path = os.path.join(self.config.image_root_data)
            destination = os.path.dirname(self.config.image_process_data)
            if not os.path.exists(destination):
                os.makedirs(destination)
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.image_process_data))}")
            destination = os.path.join(self.config.image_process_data)
            for file in os.listdir(path):
                image = cv2.imread(path + file)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, (240,180))
                image = Image.fromarray(image)
                image.save(os.path.join(destination, file))
            validation_process_status = 1
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"process resize image: {validation_process_status}")
        except Exception as e:
            raise e