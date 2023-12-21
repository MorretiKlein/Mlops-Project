import mlflow
from urllib.parse import urlparse
from MLOps_project import logger
from MLOps_project.entity.config_entity import * 

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme # get registry of MLflow

        if tracking_url_type_store != "file":
            logger.info("Logging into MLflow...")
            with mlflow.start_run():
                mlflow.log_params(self.config.params)
                mlflow.log_artifacts(self.config.root_dir)
        else:
            logger.warning("MLflow is configured to store data in local files.")