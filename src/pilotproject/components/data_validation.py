from src.pilotproject.entity.config_entity import DataValidationConfig
import pandas as pd
from src.pilotproject import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config=config
        
    def validate_all_columns(self) -> bool:
        validation_status=None
        unzip_data_dir = self.config.unzip_data_dir
        expected_column_names = self.config.all_schema.keys()
        STATUS_FILE = self.config.STATUS_FILE

        data = pd.read_csv(unzip_data_dir)
        data_column_names = set(data.columns)
        expected_column_names = set(expected_column_names)

        logger.info("Performing data validation")
        if expected_column_names == data_column_names:
            validation_status=True
        else:
            validation_status=False

        with open(STATUS_FILE, 'w') as file:
            logger.info(f"Writing validation status to file at '{STATUS_FILE}'")
            file.write(f'Validation Status: {validation_status}')

        return validation_status