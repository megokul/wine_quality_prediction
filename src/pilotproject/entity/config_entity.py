from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    Configuration for data ingestion component.
    """
    root_dir: Path  
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    """
    Configuration for data validation component.
    """
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: Path
    all_schema: dict  # Expected column names and schema


@dataclass
class DataTransformationConfig:
    """
    Configuration for data transformation component.
    """
    root_dir: Path
    data_path: Path
    STATUS_FILE: Path


@dataclass
class ModelTrainerConfig:
    """
    Configuration for model training component.
    """
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str  # File name to save the trained model
    alpha: float     # Hyperparameter for ElasticNet
    l1_ratio: float  # Hyperparameter for ElasticNet
    target_column: dict


@dataclass
class ModelEvaluationConfig:
    """
    Configuration for model evaluation component.
    """
    root_dir: Path
    test_data_path: Path
    model_path: Path
    test_metric_file_path: Path
    target_column: dict
    mlflow_uri: str
    all_params: dict  # All model parameters to log with MLflow


@dataclass
class ModelPredictionConfig:
    """
    Configuration for model prediction component.
    """
    root_dir: Path
    model_path: Path
    predictions_file_path: Path
    target_column: str  # Name of the column being predicted
    columns: dict       # All input feature columns (from schema)
