import os
from dotenv import load_dotenv
from src.pilotproject import logger

from src.pilotproject.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pilotproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.pilotproject.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pilotproject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pilotproject.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

# ===================================
# 🔹 Pipeline Entry Point
# ===================================

"""
Main script to run all ML pipeline stages sequentially:
- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation
"""

# Load environment variables (e.g., for MLflow URI)
load_dotenv()

# ==============================
# 🔸 Data Ingestion Stage
# ==============================
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
except Exception as e:
    logger.exception(e)
    raise

# ==============================
# 🔸 Data Validation Stage
# ==============================
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
except Exception as e:
    logger.exception(e)
    raise

# ==============================
# 🔸 Data Transformation Stage
# ==============================
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
except Exception as e:
    logger.exception(e)
    raise

# ==============================
# 🔸 Model Trainer Stage
# ==============================
STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
except Exception as e:
    logger.exception(e)
    raise

# ==============================
# 🔸 Model Evaluation Stage
# ==============================
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
except Exception as e:
    logger.exception(e)
    raise
