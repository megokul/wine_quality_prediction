from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.model_prediction import ModelPrediction


class PredictionPipeline:
    def __init__(self):
        pass

    def initiate_prediction(self, data):
        config=ConfigurationManager()
        model_prediction_config=config.get_model_prediction_config()
        model_prediction=ModelPrediction(model_prediction_config)
        prediction=model_prediction.predict(data)

        return prediction