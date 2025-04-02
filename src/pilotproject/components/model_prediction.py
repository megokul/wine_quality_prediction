from src.pilotproject.entity.config_entity import ModelPredictionConfig
import joblib
from pathlib import Path
from src.pilotproject import logger
import pandas as pd
from typing import Any
import numpy as np

class ModelPrediction:
    """
    Handles prediction using a trained model and writes output to a CSV file.

    Responsibilities:
    - Load the trained model.
    - Predict based on input features.
    - Format predictions with feature columns.
    - Save results to a prediction file.
    """

    def __init__(self, config: ModelPredictionConfig):
        """
        Initializes the ModelPrediction class with the given configuration.

        Parameters:
            config (ModelPredictionConfig): Contains paths, columns, and prediction output location.
        """
        self.config = config

    def predict(self, data: Any) -> np.ndarray:
        """
        Predicts outcomes using the trained model and saves the result to a file.

        Parameters:
            data (Any): Input data to predict on (e.g., numpy array or compatible DataFrame).

        Returns:
            np.ndarray: Prediction results.
        """
        try:
            model_path = self.config.model_path
            predictions_file_path = self.config.predictions_file_path

            # Extract column names from config
            all_columns = list(self.config.columns.keys())  # Full list of columns from schema

            target_column = self.config.target_column  # Extract target column name

            logger.info("Loading model from path")
            model = joblib.load(Path(model_path))  # Load model

            logger.info("Generating predictions")
            prediction = model.predict(data)  # Perform prediction

            # Remove the target column to get feature columns
            feature_columns = all_columns.copy()
            feature_columns.remove(target_column)

            # Create a DataFrame from the input data using feature columns
            data_with_predictions = pd.DataFrame(data, columns=feature_columns)
            data_with_predictions['quality'] = prediction  # Append predictions as a new column

            predictions_path = Path(predictions_file_path)
            logger.info(f"Writing predictions to: '{predictions_path}'")

            # Append if file exists; otherwise create new file with header
            if predictions_path.exists():
                data_with_predictions.to_csv(predictions_path, mode='a', header=False, index=False)
            else:
                data_with_predictions.to_csv(predictions_path, index=False)

            return prediction

        except FileNotFoundError as fnf_error:
            logger.error(f"Model file not found at: '{self.config.model_path}'. Details: {fnf_error}")
            raise

        except Exception as e:
            logger.error(f"An error occurred during prediction: {e}")
            raise
