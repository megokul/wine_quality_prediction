from src.pilotproject.config.configuration import ConfigurationManager
from src.pilotproject.components.data_transformation import DataTransformation
from src.pilotproject import logger

STAGE_NAME='Data Transformation'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(data_transformation_config)
        data_transformation.train_test_splitting()

if __name__=='__main__':
    try:
        logger.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
        obj=DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        raise e