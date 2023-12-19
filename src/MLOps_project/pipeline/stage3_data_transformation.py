from MLOps_project.config.configuration import *
from MLOps_project.compoment.data_transformation import *
from MLOps_project import logger

STAGE_NAME = "DATA TRANSFORMATION"
class DataTransformation_Stage():
    def __init__(self):
        pass
    def main():
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()
        data_transformation.image_splitting()
if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = DataTransformation_Stage()
        obj.main()
        logger.info(f"{STAGE_NAME} finished")
    except Exception as e:
        logger.exception(e)
        raise e
