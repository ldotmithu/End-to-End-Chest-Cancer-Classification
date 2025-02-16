from cnnProject.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        ingestion = DataIngestion()
        ingestion.download_from_url()
        ingestion.unzip_operation()