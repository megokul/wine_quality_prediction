import os
from src.pilotproject.constants import * 
from src.pilotproject.utils.common import read_yaml, create_directories
from src.pilotproject.entity.config_entity import (
    DataIngestionConfig, 
    DataValidationConfig, 
    DataTransformationConfig, 
    ModelTrainerConfig, 
    ModelEvaluationConfig,
    ModelPredictionConfig
)

class ConfigurationManager:
    """
    Reads and manages all configuration sections for the pipeline components.

    Responsibilities:
    - Load configuration, parameters, and schema YAML files.
    - Return structured config dataclasses for each pipeline stage.
    - Ensure necessary directories are created before pipeline execution.
    """

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):
        """
        Initializes the ConfigurationManager by loading YAML files and creating the artifact root directory.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories(self.config.artifacts_root)  # Ensure base artifacts directory exists

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Prepares and returns configuration for data ingestion.

        Returns:
            DataIngestionConfig: Configuration for the data ingestion stage.
        """
        config = self.config.data_ingestion
        create_directories(config.root_dir)

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Prepares and returns configuration for data validation.

        Returns:
            DataValidationConfig: Configuration for the data validation stage.
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories(config.root_dir)

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Prepares and returns configuration for data transformation.

        Returns:
            DataTransformationConfig: Configuration for the data transformation stage.
        """
        config = self.config.data_transformation
        create_directories(config.root_dir)

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            STATUS_FILE=config.STATUS_FILE
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Prepares and returns configuration for model training.

        Returns:
            ModelTrainerConfig: Configuration for the model training stage.
        """
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories(config.root_dir)

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.target_column,
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Prepares and returns configuration for model evaluation.

        Returns:
            ModelEvaluationConfig: Configuration for the model evaluation stage.
        """
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories(config.root_dir)

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            test_metric_file_path=config.test_metric_file_path,
            target_column=schema.target_column,
            all_params=params,
            mlflow_uri=os.getenv("MLFLOW_TRACKING_URI")
        )

        return model_evaluation_config

    def get_model_prediction_config(self) -> ModelPredictionConfig:
        """
        Prepares and returns configuration for model prediction.

        Returns:
            ModelPredictionConfig: Configuration for the model prediction stage.
        """
        config = self.config.model_prediction
        col_schema = self.schema.COLUMNS
        target_schema = self.schema.TARGET_COLUMN
        create_directories(config.root_dir)

        model_prediction_config = ModelPredictionConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            predictions_file_path=config.predictions_file_path,
            target_column=target_schema.target_column,
            columns=col_schema
        )

        return model_prediction_config
