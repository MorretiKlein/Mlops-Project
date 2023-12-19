from MLOps_project.config.configuration import *
from MLOps_project.compoment.data_validation_preprocess import *
from MLOps_project import logger

STAGE_NAME = "DATA VALIDATE AND PREPROCESS STAGE"
class Data_validate_preprocess_stage:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation_process = DataValidation_Preprocess(config=data_validation_config)
        data_validation_process.open_csv()
        data_validation_process.validate_columns()
        data_validation_process.drop_duplicate()
        data_validation_process.process_image()
if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = Data_validate_preprocess_stage()
        obj.main()
        logger.info(f"{STAGE_NAME} finished")
    except Exception as e:
        logger.exception(e)
        raise e