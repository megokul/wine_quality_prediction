import os
import urllib.request as request
from src.pilotproject import logger
from zipfile import ZipFile
from src.pilotproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    """
    Handles the data ingestion process:
    - Downloads the dataset from a specified URL.
    - Extracts the contents of the downloaded zip file.
    """

    def __init__(self, config: DataIngestionConfig):
        """
        Initializes the DataIngestion class with a configuration object.

        Parameters:
            config (DataIngestionConfig): Configuration containing paths and URLs
        """
        self.config = config

    def download_file(self) -> None:
        """
        Downloads the dataset from the source URL to a local file path.

        - Skips downloading if the file already exists.
        - Logs download metadata upon success.

        Returns:
            None
        """
        if not os.path.exists(self.config.local_data_file):  # Download only if the file doesn't exist
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )  # Download file from URL to specified local path

            logger.info(f"File downloaded successfully: '{filename}'")
            logger.debug(f"Download headers:\n{header}")
        else:
            logger.info(f"File already exists at: '{self.config.local_data_file}' — skipping download")

    def extract_zip(self) -> None:
        """
        Extracts the downloaded zip file into the specified directory.

        - Ensures the target directory exists.
        - Unzips all contents of the downloaded file.
        - Logs success or failure during extraction.

        Returns:
            None
        """
        unzip_dir = self.config.unzip_dir  # Target directory for extracted files
        local_data_file = self.config.local_data_file  # Path to the downloaded zip file

        os.makedirs(unzip_dir, exist_ok=True)  # Ensure the directory exists

        try:
            with ZipFile(local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)  # Extract all files
                logger.info(f"Extracted '{local_data_file}' into '{unzip_dir}'")
        except Exception as e:
            logger.error(f"Failed to extract '{local_data_file}' to '{unzip_dir}': {e}")
            raise  # Re-raise the exception for upstream handling
