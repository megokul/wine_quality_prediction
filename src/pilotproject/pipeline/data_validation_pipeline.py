from src.pilotproject.components.data_validation import DataValidation
from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    """
    Orchestrates the data validation stage of the pipeline.

    Responsibilities:
    - Loads validation configuration.
    - Executes schema validation on the raw dataset.
    """

    def __init__(self):
        pass

    def initiate_data_validation(self):
        """
        Executes the data validation workflow:
        - Retrieves config.
        - Performs column/schema validation.
        """
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
    except Exception as e:
        logger.exception(e)
        raise
