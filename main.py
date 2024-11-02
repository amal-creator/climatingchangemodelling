from climatingchangemodelling.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from climatingchangemodelling.pipeline.stage_02_data_validation import DataValidationTrainingPipeline   
from climatingchangemodelling.logging import logger


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'{STAGE_NAME} started')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'{STAGE_NAME} completed successfully')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data validation Stage'

try:
    logger.info(f'{STAGE_NAME} started')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'{STAGE_NAME} completed successfully')
except Exception as e:
    logger.exception(e)
    raise e