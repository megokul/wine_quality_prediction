from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.model_evaluation import ModelEvaluation
from src.pilotproject import logger

STAGE_NAME='Model Evaluation Stage'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate_log_with_mlflow()


if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
        obj=ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        raise e