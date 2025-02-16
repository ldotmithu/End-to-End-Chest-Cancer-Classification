from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir:Path = "artifacts/data_ingestion"
    URL:str = "https://drive.google.com/file/d/1M5CCFKlqeqcfpIL5fu672pkTv2UbgEUj/view?usp=sharing"
    local_data_path:Path = "artifacts/data_ingestion/data.zip"
    unzip_dir:Path = "artifacts/data_ingestion"
    