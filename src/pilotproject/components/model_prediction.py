from src.pilotproject.entity.config_entity import ModelPredictionConfig
import joblib
from pathlib import Path
from src.pilotproject import logger
import pandas as pd

class ModelPrediction:
    def __init__(self, config: ModelPredictionConfig):
        self.config=config

    def predict(self, data):
        model_path=self.config.model_path
        predictions_file_path=self.config.predictions_file_path

        logger.info("Load model")
        model=joblib.load(Path(model_path))
        logger.info("Generate prediction")
        prediction=model.predict(data)

        columns = ['fixed_acidity',
                   'volatile_acidity',
                   'citric_acid',
                   'residual_sugar',
                   'chlorides',
                   'free_sulfur_dioxide',
                   'total_sulfur_dioxide',
                   'density',
                   'pH',
                   'sulphates',
                   'alcohol']
        
        # Convert the numpy array to a DataFrame
        data_with_predictions = pd.DataFrame(data, columns=columns)

        data_with_predictions['prediction'] = prediction

        # Now assign the predictions as a new column
        data_with_predictions['prediction'] = prediction

        logger.info("Write prediction to file path: '{predictions_file_path}'")
        if Path(predictions_file_path).exists():
            data_with_predictions.to_csv(Path(predictions_file_path), mode='a', header=False, index=False)
        else:
            data_with_predictions.to_csv(Path(predictions_file_path), index=False)

        return prediction
