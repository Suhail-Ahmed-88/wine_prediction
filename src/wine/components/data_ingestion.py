import os
import urllib.request as request
import zipfile
from src.wine import logging
from src.wine.utils.common import get_size
from pathlib import Path
from src.wine.entity.config_entity import DataIngestionConfig

    
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)  # Initialize logger

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            self.logger.info(f"{filename} downloaded! with the following info: \n{headers}")
        else:
            self.logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the ZIP file specified in the config to the designated directory.
        """
        zip_file_path = self.config.local_data_file
        extract_to = self.config.unzip_dir
        
        try:
            # Check if the file exists
            if not os.path.exists(zip_file_path):
                raise ValueError(f"The file {zip_file_path} does not exist.")

            # Check if the file is a valid ZIP file
            if not zipfile.is_zipfile(zip_file_path):
                raise ValueError(f"The file {zip_file_path} is not a valid ZIP file.")

            # Create the extraction directory if it doesn't exist
            os.makedirs(extract_to, exist_ok=True)

            # Extract the ZIP file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            
            self.logger.info(f"Successfully extracted {zip_file_path} to {extract_to}")

        except Exception as e:
            self.logger.error(f"An error occurred while extracting the ZIP file: {e}")

