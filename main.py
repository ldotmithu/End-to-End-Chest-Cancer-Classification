from cnnProject import logging
from cnnProject.Pipeline.Stages_of_Pipeline import (DataIngestionPipeline,PrepareBaseModelPipeline,
ModelTrainerPipeline,ModelEvaluationPipeline)


'''
try:
    logging.info(">>>>>>>>>>Data Ingestion>>>>>>>")
    ingestion = DataIngestionPipeline()
    ingestion.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e


try:
    logging.info(">>>>>>>>>>Prepare Base Model>>>>>>>")
    base_model = PrepareBaseModelPipeline()
    base_model.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e


try:
    logging.info(">>>>>>>>>>Prepare Base Model>>>>>>>")
    trainer = ModelTrainerPipeline()
    trainer.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e
'''
try:
    logging.info(">>>>>>>>>>Prepare Base Model>>>>>>>")
    evaluation = ModelEvaluationPipeline()
    evaluation.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e