from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.model_evaluation import ModelEvaluation
from src.pilotproject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    """
    Orchestrates the model evaluation stage of the pipeline.

    Responsibilities:
    - Loads model evaluation configuration.
    - Evaluates the model using test data.
    - Logs metrics and model using MLflow.
    """

    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        """
        Executes the model evaluation workflow:
        - Loads test data and trained model.
        - Computes evaluation metrics.
        - Logs parameters, metrics, and model to MLflow.
        """
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate_log_with_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n{'x' * 10}")
    except Exception as e:
        logger.exception(e)
        raise
