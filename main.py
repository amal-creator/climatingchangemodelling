from climatingchangemodelling.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from climatingchangemodelling.logging import logger

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'{STAGE_NAME} started')
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f'{STAGE_NAME} completed successfully')
except Exception as e:
    logger.exception(e)
    raise e