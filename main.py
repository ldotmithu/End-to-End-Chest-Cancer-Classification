from cnnProject import logging
from cnnProject.Pipeline.Stages_of_Pipeline import DataIngestionPipeline



try:
    logging.info(">>>>>>>>>>Data Ingestion>>>>>>>")
    ingestion = DataIngestionPipeline()
    ingestion.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e