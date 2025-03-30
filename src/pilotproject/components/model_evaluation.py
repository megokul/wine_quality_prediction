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
    def __init__(self, config: ModelEvaluationConfig):
        self.config=config

    def eval_metrics(self, actual, preds):
        rmse=np.sqrt(mean_squared_error(actual, preds))
        mae=mean_absolute_error(actual, preds)
        r2=r2_score(actual, preds)

        return rmse, mae, r2
    
    def evaluate_log_with_mlflow(self):
        test_data_path=self.config.test_data_path
        model_path=self.config.model_path
        target_column=self.config.target_column
        mlflow_uri=self.config.mlflow_uri
        test_metric_file_path=self.config.test_metric_file_path
        all_params=self.config.all_params

        test_data=pd.read_csv(test_data_path)
        logger.info('Read test data')
        
        model=joblib.load(model_path)
        logger.info('Load model')
    
        x_test=test_data.drop(target_column, axis=1)
        y_test=test_data[[target_column]]

        mlflow.set_registry_uri(mlflow_uri)
        tracking_uri_type_store=urlparse(mlflow.get_registry_uri()).scheme

        logger.info('Start tracking with MLFlow')
        with mlflow.start_run():
            preds_test=model.predict(x_test)
            (rmse, mae, r2)=self.eval_metrics(y_test, preds_test)
            logger.info('evaluation metrics generated')

            test_scores = {
                'rmse': rmse,
                'mae': mae,
                'r2': r2
            }

            save_json(Path(test_metric_file_path), test_scores)
            logger.info(f"Save test metrics at path : '{test_metric_file_path}'")

            mlflow.log_params(all_params)
            logger.info('Log model params')

            mlflow.log_metrics(test_scores)
            logger.info('Log test metrics with MLFlow')

            logger.info(f"MLFlow uri tracking type: '{tracking_uri_type_store}'")
            if tracking_uri_type_store!='file':
                mlflow.sklearn.log_model(model, 'model', registered_model_name='ElasticNet_model', input_example=x_test.iloc[:1])
            else:
                mlflow.sklearn.log_model(model, 'model', input_example=x_test.iloc[:1])