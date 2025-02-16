from cnnProject.components.data_ingestion import DataIngestion
from cnnProject.components.prepare_base_model import PrepareBaseModel

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        ingestion = DataIngestion()
        ingestion.download_from_url()
        ingestion.unzip_operation()
        
       
class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    def main(self):
        base_model = PrepareBaseModel()
        base_model.prepare_base_model() 
        base_model.get_update_model()       
        