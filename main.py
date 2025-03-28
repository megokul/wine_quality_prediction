from src.pilotproject import logger
from src.pilotproject.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pilotproject.pipeline.data_validation_pipeline import DataValidationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
except Exception as e:
    logger.exception(e)
    raise(e)

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
    obj=DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
except Exception as e:
    logger.exception(e)
    raise e