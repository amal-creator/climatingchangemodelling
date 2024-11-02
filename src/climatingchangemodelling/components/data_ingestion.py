
import os
import zipfile
from climatingchangemodelling.utils.common import get_size
from climatingchangemodelling.logging import logger
import urllib.request as request
from climatingchangemodelling.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config = DataIngestionConfig):
        self.config = config

    def download_data(self):
        # Download data from the source
        if not os.path.exists(self.config.local_data_files) :
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_files
            )
            logger.info(f" {filename} downloaded with following info : \n {headers}") 
        
        else :
            logger.info(f"file already exist of size : {get_size(Path(self.config.local_data_files))}")

    def extract_zip_file(self):
        unzip_file = self.config.unzip_dir

        os.makedirs(unzip_file, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
            zip_ref.extractall(unzip_file)
            logger.info(f"Extracted zip file to : {unzip_file}")
