from Deep_Learning_Classification_project import logger
from Deep_Learning_Classification_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

SATGE_NAME = "Data Ingestion Stage"
try:
   logger.info(f">>>>>> stage {SATGE_NAME} started <<<<<<")
   obj = DataIngestionTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {SATGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e     