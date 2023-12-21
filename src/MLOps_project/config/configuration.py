from MLOps_project.constant import *
from MLOps_project.utils.common import read_yaml, create_directories
from MLOps_project.entity.config_entity import * 
class ConfigurationManager: # manage: read and use files config
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        # create a root directory to storage data


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL_label=config.source_URL_label,
            local_data_file=config.local_data_file,
            source_URL_for_image = config.source_URL_for_image,
            source_code_download = config.source_code_download
        )
        # Helps get detailed configuration for data download.
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidation_PreprocessConfig:
        config = self.config.data_validation_and_preprocess
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidation_PreprocessConfig(
            root_dir = config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            label_root_data = config.label_root_data,
            label_process_data = config.label_process_data,
            image_root_data= config.image_root_data,
            image_process_data= config.image_process_data,
            choose_schema = schema
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            label_process_data=config.label_process_data,
            image_train_data = config.image_train_data,
            image_test_data = config.image_test_data,
            image_root_data= config.image_root_data
        )

        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.yolov5

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            all_data = config.all_data,
            image_train_data = config.image_train_data,
            image_test_data = config.image_test_data,
            params = params
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.yolov5
        schema =  self.schema.COLUMNS

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            dataset_path = config.dataset_path,
            schema = [schema.XMin, schema.XMax, schema.YMin, schema.YMax],
            params = params ,
            mlflow_uri= "https://dagshub.com/MorretiKlein/Mlops-Project",
           
        )

        return model_evaluation_config