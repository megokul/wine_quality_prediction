from src.pilotproject.entity.config_entity import DataValidationConfig
import pandas as pd
from src.pilotproject import logger

class DataValidation:
    """
    Handles validation of the raw dataset against the expected schema.

    Responsibilities:
    - Reads the unzipped CSV data.
    - Compares column names with the expected schema.
    - Logs and writes the validation result to a status file.
    """

    def __init__(self, config: DataValidationConfig):
        """
        Initializes the DataValidation class with the given config.

        Parameters:
            config (DataValidationConfig): Contains schema, paths, and status file location.
        """
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates whether the columns in the raw CSV match the expected schema.

        - Reads the dataset from the configured path.
        - Compares actual column names with those specified in the schema.
        - Writes the validation result to a status file.
        - Logs progress and errors.

        Returns:
            bool: True if validation passes, False otherwise.
        """
        try:
            validation_status = None  # Will hold the result (True/False)
            unzip_data_dir = self.config.unzip_data_dir  # Path to the unzipped dataset
            expected_column_names = set(self.config.all_schema.keys())  # Schema from config
            STATUS_FILE = self.config.STATUS_FILE  # Path to store validation result

            # Read the CSV data
            data = pd.read_csv(unzip_data_dir)
            data_column_names = set(data.columns)  # Actual column names from dataset

            logger.info("Performing data validation")

            # Compare expected vs actual columns
            if expected_column_names == data_column_names:
                validation_status = True
                logger.info("Column validation passed")
            else:
                validation_status = False
                logger.warning("Column validation failed")
                logger.debug(f"Expected columns: {expected_column_names}")
                logger.debug(f"Found columns: {data_column_names}")

            # Write validation status to a file
            with open(STATUS_FILE, 'w') as file:
                logger.info(f"Writing validation status to file at '{STATUS_FILE}'")
                file.write(f'Validation Status: {validation_status}')

            return validation_status

        except FileNotFoundError as fnf_error:
            logger.error(f"Data file not found at: '{self.config.unzip_data_dir}'. Details: {fnf_error}")
            raise

        except Exception as e:
            logger.error(f"An error occurred during data validation: {e}")
            raise
