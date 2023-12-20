from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig: # class storage config of data ingestion
    root_dir: Path
    source_URL_label: str
    local_data_file: Path
    source_URL_for_image: Path
    source_code_download: Path
    
@dataclass(frozen=True) #1 class immutable
class DataValidation_PreprocessConfig:
    root_dir: Path
    STATUS_FILE: str
    label_root_data: Path
    label_process_data: Path
    image_root_data: Path
    image_process_data: Path
    choose_schema: dict

@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    label_process_data: Path
    image_train_data: Path
    image_test_data: Path
    image_root_data: Path

@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir: Path
    all_data: Path
    image_train_data: Path
    image_test_data: Path
    model_name: str
    