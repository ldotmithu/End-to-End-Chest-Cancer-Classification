from cnnProject.components.data_ingestion import DataIngestion
from cnnProject.components.prepare_base_model import PrepareBaseModel
from cnnProject.components.model_trainer import ModelTrainer
from cnnProject.components.model_evaluation import ModelEvaluation

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
        
class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        trainer = ModelTrainer()
        trainer.train()
        
class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        evaluation = ModelEvaluation()
        evaluation.model_evaluation()        