from src.pilotproject.entity.config_entity import ModelTrainerConfig
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
import os
from src.pilotproject import logger
from typing import NoReturn

class ModelTrainer:
    """
    Handles training of a regression model using ElasticNet.

    Responsibilities:
    - Load training and testing datasets.
    - Split features and target column.
    - Train the ElasticNet model.
    - Save the trained model to disk.
    """

    def __init__(self, config: ModelTrainerConfig):
        """
        Initializes the ModelTrainer with configuration.

        Parameters:
            config (ModelTrainerConfig): Contains training parameters, file paths, and output model location.
        """
        self.config = config

    def train(self) -> NoReturn:
        """
        Trains the ElasticNet model and saves it to a specified path.

        - Loads training and test datasets.
        - Splits data into features and target.
        - Trains an ElasticNet model using configured hyperparameters.
        - Saves the trained model as a joblib file.

        Returns:
            None
        """
        try:
            # Extract paths and hyperparameters from config
            train_data_path = self.config.train_data_path
            test_data_path = self.config.test_data_path
            target_column = self.config.target_column
            alpha = self.config.alpha
            l1_ratio = self.config.l1_ratio
            model_path = os.path.join(self.config.root_dir, self.config.model_name)

            logger.info("Reading training data")
            train_data = pd.read_csv(train_data_path)

            logger.info("Reading test data")
            test_data = pd.read_csv(test_data_path)

            logger.info("Extracting features and target from training data")
            x_train = train_data.drop(target_column, axis=1)  # Input features
            y_train = train_data[[target_column]]             # Target column

            # Initialize and train ElasticNet model
            lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
            logger.info(f"Training ElasticNet model with alpha={alpha}, l1_ratio={l1_ratio}")
            lr.fit(x_train, y_train)
            logger.info("Model training completed")

            # Save trained model to disk
            joblib.dump(lr, model_path)
            logger.info(f"Trained model saved to: '{model_path}'")

        except FileNotFoundError as fnf_error:
            logger.error(f"One of the dataset files was not found. Details: {fnf_error}")
            raise

        except Exception as e:
            logger.error(f"An error occurred during model training: {e}")
            raise
