# Mlops-Project: Person detection and track with MLflow

# I use MIAP dataset
MIAP is a dataset created by obtaining a new set of annotations on a subset of the Open Images dataset, containing bounding boxes and attributes for all of the people visible in those images, as the original Open Images dataset annotations are not exhaustive, with bounding boxes and attribute labels for only a subset of the classes in each image.
I only use a sample of dataset to use for detect person, you can use all or another sample for trainning(Details are in the section data_ingestion)

## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manage in src config
6. Update the component
7. Update the pipeline
8. Update the main.py
9. Create the prediction.py
9. Update the dvc.yaml/app.py

# to run and check repository
### STEPS:

Clone the repository

```bash
https://github.com/MorretiKlein/Mlops-Project

### STEP 01- Create a conda environment after opening the repository
```bash
conda create -n ML_Ops python=3.10 -y
```

```bash
conda activate ML_ops
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```
Now,
```bash
open up you local host and port
```

## MLflow

let read clealy documentation of mlflow

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/MorretiKlein/Mlops-Project.mlflow \
MLFLOW_TRACKING_USERNAME=MorretiKlein \
MLFLOW_TRACKING_PASSWORD=c1c64d907121622a72df895d266f6d75a86c8d50 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/MorretiKlein/Mlops-Project.mlflow

export MLFLOW_TRACKING_USERNAME=MorretiKlein 

export MLFLOW_TRACKING_PASSWORD=c1c64d907121622a72df895d266f6d75a86c8d5
```

### Final test  
1. run the file app.py
2. Visit http://localhost:5000/ in your browser to view webcam video and predict objects.
3. When finished, you can stop the application by returning to the terminal and pressing Ctrl+C to stop the Flask server.