from src.pilotproject.config.configuration import DataTransformationConfig
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.pilotproject import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config

    def train_test_splitting(self):
        data_path=self.config.data_path
        root_dir=self.config.root_dir
        data=pd.read_csv(data_path)

        train, test = train_test_split(data)
        logger.info("Splited data into training and testing sets")

        train_data_path=os.path.join(root_dir, 'train.csv')
        train.to_csv(train_data_path, index=False)
        logger. info(f"Training data set saved at path: '{train_data_path}'")
        logger. info(f"Shape of training data set: {train.shape}")

        test_data_path=os.path.join(root_dir, 'test.csv')
        test.to_csv(test_data_path, index=False)
        logger. info(f"Testing data set saved at path: '{test_data_path}'")
        logger. info(f"Shape of testing data set: {test.shape}")

