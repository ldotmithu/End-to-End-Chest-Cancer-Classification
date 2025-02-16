from pathlib import Path
import os 
from cnnProject import logging
import yaml

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
            