from src.pilotproject.config.configuration import DataTransformationConfig
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.pilotproject import logger

class DataTransformation:
    """
    Handles the transformation of raw data into train-test splits.

    Responsibilities:
    - Loads the preprocessed CSV dataset.
    - Splits the dataset into training and testing sets.
    - Saves the split files to disk.
    - Validates the dataset before processing.
    """

    def __init__(self, config: DataTransformationConfig):
        """
        Initializes the DataTransformation class with the given config.

        Parameters:
            config (DataTransformationConfig): Contains paths and settings for data transformation.
        """
        self.config = config

    def train_test_splitting(self, test_size: float = 0.25, random_state: int = 42) -> None:
        """
        Loads the dataset, splits it into training and testing sets, and saves both to disk.

        - Uses specified test size and random state for reproducibility.
        - Saves the resulting CSV files in the configured root directory.
        - Logs output paths, shapes, and any issues encountered during the process.

        Parameters:
            test_size (float): Proportion of data to use as the test set.
            random_state (int): Random seed for reproducibility.

        Returns:
            None
        """
        try:
            data_path = self.config.data_path  # Path to the preprocessed CSV data
            root_dir = self.config.root_dir    # Directory to save the train/test files

            data = pd.read_csv(data_path)  # Load the dataset from CSV
            logger.info(f"Loaded dataset from: '{data_path}'")

            if data.empty:
                logger.error("The dataset is empty. Cannot proceed with splitting.")
                raise ValueError("Input data is empty.")

            # Perform the train-test split with reproducibility
            train, test = train_test_split(data, test_size=test_size, random_state=random_state)
            logger.info(f"Split data into train and test sets with test_size={test_size}")

            # Save training data
            train_data_path = os.path.join(root_dir, 'train.csv')
            train.to_csv(train_data_path, index=False)
            logger.info(f"Training dataset saved at: '{train_data_path}'")
            logger.info(f"Training data shape: {train.shape}")

            # Save testing data
            test_data_path = os.path.join(root_dir, 'test.csv')
            test.to_csv(test_data_path, index=False)
            logger.info(f"Testing dataset saved at: '{test_data_path}'")
            logger.info(f"Testing data shape: {test.shape}")

        except FileNotFoundError as fnf_error:
            logger.error(f"Data file not found at: '{self.config.data_path}'. Details: {fnf_error}")
            raise

        except Exception as e:
            logger.error(f"An error occurred during train-test splitting: {e}")
            raise
