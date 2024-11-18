import os
from src.wine.components.data_validation import DataValidation
from src.wine.entity.config_entity import DataValidationConfig
from src.wine.config.configuration import ConfigurationManager
from src.wine import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
        # self.data_validation_config = DataValidationConfig()
        # self.data_validation = DataValidation(config=self.data_validation_config)

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e