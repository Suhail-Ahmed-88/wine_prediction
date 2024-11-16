
from src.wine import logger
from src.wine.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# logger.info("Welcome to Custom Logging")


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e