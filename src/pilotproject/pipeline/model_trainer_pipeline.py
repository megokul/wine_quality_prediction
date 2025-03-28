from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.model_trainer import ModelTrainer
from src.pilotproject import logger

STAGE_NAME="Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(model_trainer_config)
        model_trainer.train()
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
        obj=ModelTrainerPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        raise e