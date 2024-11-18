
from src.wine import logger
from src.wine.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.wine.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

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


Stage_name = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {Stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e