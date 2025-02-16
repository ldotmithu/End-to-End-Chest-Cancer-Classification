from cnnProject.config.config_entity import DataIngestionConfig
from cnnProject import logging
import os 
import zipfile
import gdown
from cnnProject.utils.common import create_dir
from pathlib import Path


class DataIngestion:
    def __init__(self):
        self.ingestion = DataIngestionConfig()
        
        create_dir(Path(self.ingestion.root_dir))
        
    def download_from_url(self):
        try:
            url_path = self.ingestion.URL
            zip_path = self.ingestion.local_data_path
            file_id = url_path.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_path)
            logging.info(f"Zip data Downloaded")
        except Exception as e:
            raise e
        
    def unzip_operation(self):
        unzip_path = self.ingestion.unzip_dir
        with zipfile.ZipFile(self.ingestion.local_data_path) as f:
            f.extractall(unzip_path)
            logging.info("Unzip the zip file")    
    
                
            
        
        
        