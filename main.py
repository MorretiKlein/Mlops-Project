from MLOps_project import logger
from MLOps_project.pipeline.stage3_data_transformation import DataTransformation_Stage
from MLOps_project.pipeline.stage1_data_ingestion import DataIngestionSTAGE
from MLOps_project.pipeline.stage2_data_validate_preprocess import Data_validate_preprocess_stage

logger.info("Welcome")
STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataIngestionSTAGE()
    obj.main()
    logger.info(f"{STAGE_NAME} finished")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "DATA VALIDATE AND PREPROCESS STAGE"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = Data_validate_preprocess_stage()
    obj.main()
    logger.info(f"{STAGE_NAME} finished")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA TRANSFORMATION"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataTransformation_Stage()
    obj.main()
    logger.info(f"{STAGE_NAME} finished")
except Exception as e:
    logger.exception(e)
    raise e
