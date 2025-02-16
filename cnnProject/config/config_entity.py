from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir:Path = "artifacts/data_ingestion"
    URL:str = "https://drive.google.com/file/d/1M5CCFKlqeqcfpIL5fu672pkTv2UbgEUj/view?usp=sharing"
    local_data_path:Path = "artifacts/data_ingestion/data.zip"
    unzip_dir:Path = "artifacts/data_ingestion"
    
@dataclass
class PrepareBaseModelConfig:
    root_dir:Path = "artifacts/base_model"
    base_model_path:Path = "artifacts/base_model/base_model.h5"
    updated_model_path:Path = "artifacts/base_model/updated_model.h5"    
    
@dataclass
class ModelTrainerConfig:
    root_dir:Path = "artifacts/trainer"
    train_model_path:Path = "artifacts/trainer/trained_model.h5"
    updated_model_path:Path = "artifacts/base_model/updated_model.h5"
    train_data_path:Path = "artifacts/data_ingestion"   
@dataclass
class ModelEvaluationConfig:
    root_dir:Path = "artifacts/evaluation"
    train_model_path:Path="artifacts/trainer/trained_model.h5"
    metrics_name:str ="metrics.json"
    
        
    