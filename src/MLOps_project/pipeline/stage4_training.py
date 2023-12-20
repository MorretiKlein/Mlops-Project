from MLOps_project.config.configuration import *
from MLOps_project.compoment.trainning import *
from MLOps_project import logger

STAGE_NAME = "Trainning"
class Trainning_Stage():
    def __init__(self):
        pass
    def main():
        config = ConfigurationManager()
        training_config = config.get_data_transformation_config()
        trainning = ModelTrainer(config=training_config)
        trainning.main()

if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = Trainning_Stage()
        obj.main()
        logger.info(f"{STAGE_NAME} finished")
    except Exception as e:
        logger.exception(e)
        raise e
