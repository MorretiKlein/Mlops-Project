from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig: # class storage config of data ingestion
    root_dir: Path
    source_URL_label: str
    local_data_file: Path
    source_URL_for_image: Path
    source_code_download: Path