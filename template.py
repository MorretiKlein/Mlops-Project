import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format= '[%(asctime)s]: %(message)s:')

project_name ="MLOps_project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/compoment/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # if filedir tồn tại thì not do
        logging.info(f"create directory: {filedir} for the file:{filename}")
    if (not os.path.exists(filepath)) or(os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"create empty file: {filepath}")
    else:
         logging.info(f"{filepath} is already extist")
                         

