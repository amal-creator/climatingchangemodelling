
from climatingchangemodelling.config.configuration import ConfigurationManager
from climatingchangemodelling.components.data_ingestion import DataIngestion



class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_injestion()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()



        

