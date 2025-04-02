from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.data_ingestion import DataIngestion
from src.pilotproject import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    """
    Orchestrates the data ingestion stage of the pipeline.

    Responsibilities:
    - Loads the data ingestion configuration.
    - Executes downloading and unzipping of raw data.
    """

    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        """
        Executes the data ingestion workflow:
        - Retrieves configuration for data ingestion.
        - Downloads data if not already present.
        - Extracts the zip file to a specified directory.
        """
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
    except Exception as e:
        logger.exception(e)
        raise
