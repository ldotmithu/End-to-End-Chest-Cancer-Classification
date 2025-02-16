from cnnProject.config.config_entity import PrepareBaseModelConfig
from cnnProject.constants.constant_config import *
from cnnProject.utils.common import create_dir,read_yaml
import tensorflow as tf 
from cnnProject import logging


class PrepareBaseModel:
    def __init__(self):
        self.base_model = PrepareBaseModelConfig()
        self.params = read_yaml(params_file_path)['CNN_MODEL']
        create_dir(self.base_model.root_dir)
        
    def prepare_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(include_top =self.params.get("INCLUDE_TOP"),
                                                       weights = self.params.get("WEIGHTS"),
                                                       input_shape = self.params.get("IMAGE_SIZE"))
        
        self.save_model(file_path=self.base_model.base_model_path,model=self.model)
        logging.info(f"Save the updated model {self.base_model.base_model_path}")
        
    
        
        for layer in self.model.layers:
            layer.trainable = False
        
        flatten = tf.keras.layers.Flatten()(self.model.output)
        prediction_layer = tf.keras.layers.Dense(units=self.params.get("CLASSES"),
                                                activation = 'softmax')(flatten) 
        
        full_model = tf.keras.models.Model(inputs=self.model.input,outputs =prediction_layer)
        
        
        full_model.compile(loss = tf.keras.losses.CategoricalCrossentropy(),
                      optimizer = tf.keras.optimizers.SGD(learning_rate=self.params.get('LEARNING_RATE')),
                      metrics = ['accuracy'],
                      )
        full_model.summary()
        
        self.save_model(file_path=self.base_model.updated_model_path,model=full_model)
        logging.info(f"Save the updated model {self.base_model.updated_model_path}")
        
    @staticmethod
    def save_model(file_path,model:tf.keras.Model):
        model.save(file_path)        
            
        
        
    
            