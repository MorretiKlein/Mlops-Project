from MLOps_project.config.configuration import *
from MLOps_project.compoment.evaluation import *
from MLOps_project import logger

STAGE_NAME = "Evaluation"
class Trainning_Stage():
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = Trainning_Stage()
        obj.main()
        logger.info(f"{STAGE_NAME} finished")
    except Exception as e:
        logger.exception(e)
        raise e
