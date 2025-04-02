from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.model_trainer import ModelTrainer
from src.pilotproject import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    """
    Orchestrates the model training stage of the pipeline.

    Responsibilities:
    - Loads training configuration and data.
    - Trains the model using the specified parameters.
    - Saves the trained model to disk.
    """

    def __init__(self):
        pass

    def initiate_model_trainer(self):
        """
        Executes the model training workflow:
        - Retrieves configuration for model training.
        - Initializes and trains the model.
        - Saves the trained model file.
        """
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
    except Exception as e:
        logger.exception(e)
        raise
