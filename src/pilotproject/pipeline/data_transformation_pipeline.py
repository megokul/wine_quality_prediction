from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.data_transformation import DataTransformation
from src.pilotproject import logger

STAGE_NAME = "Data Transformation"

class DataTransformationPipeline:
    """
    Orchestrates the data transformation stage of the pipeline.

    Responsibilities:
    - Reads validation status from file.
    - If validation passes, proceeds with train-test split.
    """

    def __init__(self):
        pass

    def initiate_data_transformation(self):
        """
        Executes the data transformation workflow:
        - Checks validation status from status file.
        - If valid, splits data into train and test sets.
        - If invalid, logs error and raises exception.
        """
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        STATUS_FILE = data_transformation_config.STATUS_FILE

        logger.info("Checking validation status...")
        with open(STATUS_FILE, 'r') as file:
            validation_status = file.read().split(" ")[-1]

            if validation_status == 'True':
                logger.info(f"Validation status: '{validation_status}' — proceeding with transformation")
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                logger.info(f"Validation status: '{validation_status}' — stopping pipeline")
                raise Exception("Data schema is not valid")


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
    except Exception as e:
        logger.exception(e)
        raise
