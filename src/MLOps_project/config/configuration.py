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