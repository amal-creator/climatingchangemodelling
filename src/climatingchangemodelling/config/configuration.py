from climatingchangemodelling.constants import *
from climatingchangemodelling.utils.common import read_yaml,create_directories
from climatingchangemodelling.entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
            self,
            config_file = CONFIG_FILE_PATH,
            params_file = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)

        create_directories([self.config.artifacts_root])


    def get_data_injestion(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])
        
        data_ingestion_config= DataIngestionConfig(
            root_dir=config.root_dir,
            source_url =  config.source_url,
            local_data_files  = config.local_data_files,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config