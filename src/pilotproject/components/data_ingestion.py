import os
import urllib.request as request
from src.pilotproject import logger
from zipfile import ZipFile
from src.pilotproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
                )
            logger.info(f"File: '{filename}' downloaded successfully with the following info: \n{header}")

        else:
            logger.info("File already exists")

    def extract_zip(self):
        unzip_dir=self.config.unzip_dir
        local_data_file=self.config.local_data_file
        os.makedirs(unzip_dir, exist_ok=True)
        with ZipFile(local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)




