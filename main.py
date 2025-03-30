import os
from dotenv import load_dotenv
from src.pilotproject import logger
from src.pilotproject.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pilotproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.pilotproject.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pilotproject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pilotproject.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


# Load from .env file to set environment variables
load_dotenv()

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


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
    obj=DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
    obj=ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Model Evaluation Stage'
try:
    logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
    obj=ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
except Exception as e:
    logger.exception(e)
    raise e