from pathlib import Path
import os 
from cnnProject import logging
import yaml,joblib

def create_dir(file_path:Path):
    try:
        os.makedirs(file_path,exist_ok=True)
        logging.info(f"{file_path} folder created")
    except Exception as e:
        raise e     
    
def read_yaml(path:Path):
    try:
        with open(path,'r') as f:
            file = yaml.safe_load(f)
            logging.info(f"Read this {path}  Yaml file ")
            return file
    except Exception as e:
        raise e        
            
def save_object(file_path,obj):
    try:
        with open(file_path,'w') as f:
            file =joblib.dump(obj,f)
            logging.info("save metrics succesfully in model evaluation ")
            return file    
    except Exception as e:
        raise e             