import os
import time
import urllib.request as request # use to download file from url
import subprocess
from MLOps_project import logger
from MLOps_project.utils.common import get_size
from pathlib import Path
from MLOps_project.entity.config_entity import * 

class DataIngestion: 
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(os.path.join(self.config.root_dir, "label_root.csv" )):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL_label,
                filename =os.path.join(self.config.root_dir, "label_root.csv" ))
            logger.info(f"{filename} download! with following info: \n{headers}")
        
        if not os.path.exists(os.path.join(self.config.root_dir, "validation.lst" )):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL_for_image,
                filename =os.path.join(self.config.root_dir, "validation.lst" ))
            logger.info(f"{filename} download! with following info: \n{headers}")

        if not os.path.exists(os.path.join(self.config.root_dir, "download.py" )):
            filename, headers = request.urlretrieve(
                url = self.config.source_code_download,
                filename =os.path.join(self.config.root_dir, "download.py" ))
            logger.info(f"{filename} download! with following info: \n{headers}")

        download_folder = self.config.local_data_file

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

        IMAGE_LIST_FILE = "artifacts\data_ingestion\\validation.lst" # self.config.root_dir +"/"+ "validation.lst"

        command = [
            "python", "artifacts\data_ingestion\download.py",
            IMAGE_LIST_FILE,
            "--download_folder=" + download_folder,
            "--num_processes=5"
        ]

        # Chạy command
        print(subprocess.list2cmdline(command))
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print("Error running the command:", e)
        