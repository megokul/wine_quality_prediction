from src.pilotproject.config.configuration import ModelEvaluationConfig
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
from src.pilotproject.utils.common import save_json
from src.pilotproject import logger
from pathlib import Path

class ModelEvaluation:
    """
    Handles evaluation of the trained model on test data and logs metrics using MLflow.

    Responsibilities:
    - Load test data and trained model.
    - Generate regression evaluation metrics (RMSE, MAE, R2).
    - Save evaluation results to JSON.
    - Log model, metrics, and parameters with MLflow.
    """

    def __init__(self, config: ModelEvaluationConfig):
        """
        Initializes the ModelEvaluation class with the given configuration.

        Parameters:
            config (ModelEvaluationConfig): Configuration object with paths and MLflow settings.
        """
        self.config = config

    def eval_metrics(self, actual: pd.Series, preds: np.ndarray) -> tuple:
        """
        Calculates regression metrics: RMSE, MAE, and R2.

        Parameters:
            actual (pd.Series): Actual target values.
            preds (np.ndarray): Predicted values from the model.

        Returns:
            tuple: (rmse, mae, r2) as floats
        """
        rmse = np.sqrt(mean_squared_error(actual, preds))
        mae = mean_absolute_error(actual, preds)
        r2 = r2_score(actual, preds)

        return rmse, mae, r2

    def evaluate_log_with_mlflow(self) -> None:
        """
        Evaluates the model and logs the results using MLflow.

        - Loads the test data and trained model.
        - Calculates evaluation metrics.
        - Saves metrics to disk.
        - Logs metrics, parameters, and model to MLflow.

        Returns:
            None
        """
        try:
            # Load paths and configs from config object
            test_data_path = self.config.test_data_path
            model_path = self.config.model_path
            target_column = self.config.target_column
            mlflow_uri = self.config.mlflow_uri
            test_metric_file_path = self.config.test_metric_file_path
            all_params = self.config.all_params

            # Load the test data
            test_data = pd.read_csv(test_data_path)
            logger.info("Loaded test dataset")

            # Load the trained model
            model = joblib.load(model_path)
            logger.info("Loaded trained model from disk")

            # Split test data into features and target
            x_test = test_data.drop(target_column, axis=1)
            y_test = test_data[[target_column]]

            # Set MLflow tracking URI
            mlflow.set_registry_uri(mlflow_uri)
            tracking_uri_type_store = urlparse(mlflow.get_registry_uri()).scheme

            logger.info("Starting MLflow run")
            with mlflow.start_run():
                preds_test = model.predict(x_test)  # Generate predictions
                rmse, mae, r2 = self.eval_metrics(y_test, preds_test)  # Evaluate metrics
                logger.info("Generated evaluation metrics")

                # Save metrics to JSON
                test_scores = {
                    "rmse": rmse,
                    "mae": mae,
                    "r2": r2
                }

                save_json(Path(test_metric_file_path), test_scores)
                logger.info(f"Saved test metrics to: '{test_metric_file_path}'")

                # Log parameters and metrics to MLflow
                mlflow.log_params(all_params)
                logger.info("Logged model parameters to MLflow")

                mlflow.log_metrics(test_scores)
                logger.info("Logged test metrics to MLflow")

                logger.info(f"MLflow tracking URI type: '{tracking_uri_type_store}'")

                # Register model if not using local file store
                if tracking_uri_type_store != "file":
                    mlflow.sklearn.log_model(
                        model,
                        "model",
                        registered_model_name="ElasticNet_model",
                        input_example=x_test.iloc[:1]
                    )
                else:
                    mlflow.sklearn.log_model(
                        model,
                        "model",
                        input_example=x_test.iloc[:1]
                    )

        except FileNotFoundError as fnf_error:
            logger.error(f"File not found during model evaluation. Details: {fnf_error}")
            raise

        except Exception as e:
            logger.error(f"An unexpected error occurred during model evaluation: {e}")
            raise
