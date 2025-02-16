from cnnProject.config.config_entity import ModelTrainerConfig
from cnnProject import logging
import tensorflow as tf 
from cnnProject.utils.common import create_dir,read_yaml
from cnnProject.constants.constant_config import *
from tensorflow import keras 
import os 
import numpy as np 

class ModelTrainer:
    def __init__(self):
        self.trainer = ModelTrainerConfig()
        self.params = read_yaml(params_file_path)['CNN_MODEL']
        
        create_dir(self.trainer.root_dir)
        
    def get_upadete_model(self):
        updated_model = tf.keras.models.load_model(self.trainer.updated_model_path)
        return updated_model
    
    def train_test_data_gen(self):   
        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale =1/255,
            horizontal_flip = True,
            validation_split = 0.2,
            zoom_range =0.1,
            rotation_range = 40,
            width_shift_range=0.2  
        ) 
        
        test_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale = 1/255,
            validation_split = 0.2)
        
        return train_datagen,test_data_gen
    
    def prepare_to_train(self):
        
        train_datagen,test_data_gen = self.train_test_data_gen()
        
        train_data = train_datagen.flow_from_directory(
            directory = os.path.join(self.trainer.train_data_path,"Chest-CT-Scan-data"),
            batch_size = self.params.get("BATCH_SIZE"),
            shuffle = True,
            subset = "training", 
            target_size = self.params.get("IMAGE_SIZE")[:-1]
        )
        
        val_data = train_datagen.flow_from_directory(
            directory = os.path.join(self.trainer.train_data_path,"Chest-CT-Scan-data"),
            shuffle = True,
            subset = "validation",
            target_size = self.params.get("IMAGE_SIZE")[:-1],
            batch_size = self.params.get("BATCH_SIZE")    
        )
        
        test_data = test_data_gen.flow_from_directory(
            directory = os.path.join(self.trainer.train_data_path,"Chest-CT-Scan-data"),
            shuffle = False,
            target_size = self.params.get("IMAGE_SIZE")[:-1],
            batch_size = self.params.get("BATCH_SIZE")    
        )
        return train_data,val_data,test_data
        
    def train(self):
        train_data ,val_data, test_data = self.prepare_to_train()
        tf.compat.v1.enable_eager_execution()
        model =self.get_upadete_model()
        
        model.fit(
            train_data,
            validation_data=val_data,
            epochs = self.params.get('EPOCHS'),
            batch_size = self.params.get('BATCH_SIZE')
        )    
        self.save_model(file_path=self.trainer.train_model_path,model=model)
        logging.info("final model saved")
        
        
        
    @staticmethod
    def save_model(file_path,model):
        """
        Saves the trained model to the specified file path.
        """
        model.save(file_path)
        return model
        