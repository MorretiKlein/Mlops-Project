from MLOps_project import logger
from MLOps_project.pipeline.stage1_data_ingestion import DataIngestionSTAGE
# logger.info("Welcome")
STAGE_NAME = "DATA INGESTION STAGE"
try:
    logger.info(f"{STAGE_NAME} started")
    obj = DataIngestionSTAGE()
    obj.main()
    logger.info(f"{STAGE_NAME} finished")
except Exception as e:
    logger.exception(e)
    raise e
