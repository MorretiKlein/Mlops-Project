from MLOps_project.config.configuration import *
from MLOps_project.compoment.data_ingestion import *
from MLOps_project import logger

STAGE_NAME = "DATA INGESTION STAGE"
class DataIngestionSTAGE:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()

if __name__ == '__main__':
    try:
        logger.info(f"{STAGE_NAME} started")
        obj = DataIngestionSTAGE()
        obj.main()
        logger.info(f"{STAGE_NAME} finished")
    except Exception as e:
        logger.exception(e)
        raise e
