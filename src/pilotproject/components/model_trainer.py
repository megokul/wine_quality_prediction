from src.pilotproject.entity.config_entity import ModelTrainerConfig
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
import os
from src.pilotproject import logger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config=config

    def train(self):
        train_data_path=self.config.train_data_path
        test_data_path=self.config.test_data_path
        target_column=self.config.target_column
        alpha=self.config.alpha
        l1_ratio=self.config.l1_ratio
        model_path=os.path.join(self.config.root_dir, self.config.model_name)

        logger.info("Read train data")
        train_data=pd.read_csv(train_data_path)
        logger.info("Read test data")
        test_data=pd.read_csv(test_data_path)

        logger.info("Extract features")
        x_train=train_data.drop(target_column, axis=1)
        x_test=test_data.drop(target_column, axis=1)
        logger.info("Extract target")
        y_train=train_data[[target_column]]
        y_test=test_data[[target_column]]

        lr=ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        logger.info("Start training model")
        lr.fit(x_train, y_train)
        logger.info("Training completed")

        joblib.dump(lr, model_path)
        logger.info(f"Model saved in path: '{model_path}'")