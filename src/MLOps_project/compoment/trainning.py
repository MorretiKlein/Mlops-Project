from ultralytics import YOLO
from MLOps_project.config.configuration import *
from MLOps_project.entity.config_entity import *
from MLOps_project import logger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def create_yaml(self, path, train_folder, val_folder):
        yaml_content = f"""\
                        path: {path}
                        train: {train_folder}
                        val: {val_folder}
                        nc: 1
                        names: ['person']
                        """
        with open('dataset.yaml', 'w') as file:
            file.write(yaml_content)

    def train(self):
        self.create_yaml(path=self.config.root_dir, train_folder=self.config.image_train_data, val_folder=self.config.image_test_data)
        model = YOLO('yolov5n.pt')
        model.train(data="dataset.yaml", epochs=self.config.params.epoch, batch=self.config.params.epoch.batch_size, project="evalution", name="model")  
    
