from src.pilotproject import logger
from src.pilotproject.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise(e)