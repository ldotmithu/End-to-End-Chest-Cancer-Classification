from pathlib import Path
import os 
from cnnProject import logging

def create_dir(file_path:Path):
    try:
        os.makedirs(file_path,exist_ok=True)
        logging.info(f"{file_path} folder created")
    except Exception as e:
        raise e     
    