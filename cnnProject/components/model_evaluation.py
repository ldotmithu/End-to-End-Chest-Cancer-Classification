from cnnProject.config.config_entity import ModelEvaluationConfig
from cnnProject.components.model_trainer import ModelTrainer
from cnnProject import logging
import tensorflow as tf 
from cnnProject.utils.common import create_dir,read_yaml,save_object
from cnnProject.constants.constant_config import *
import numpy as np 
from sklearn.metrics import classification_report
import json,os

class ModelEvaluation:
    def __init__(self):
        self.evaluation = ModelEvaluationConfig()
        self.params = read_yaml(params_file_path)
        
        create_dir(self.evaluation.root_dir)
        
    def load_model(self):
        model = tf.keras.models.load_model(self.evaluation.train_model_path)
        return model    
        
    def model_evaluation(self):
        trainer = ModelTrainer()
        train_data,val_data,test_data = trainer.prepare_to_train() 
        
        model = self.load_model()   
        y_true = test_data.classes
        
        #prd = model.predict(test_data)
        #y_pred = np.argmax(prd, axis=1)
        #print(classification_report(y_true, y_pred, target_names=test_data.class_indices.keys()))
        metrics = model.evaluate(test_data)
        logging.info(f"metrices :{metrics}")
        metrics_data = {
            "loss": metrics[0],  # Loss value
            "accuracy": metrics[1]  # Accuracy (modify if you have more metrics)
        }
        
        

