import os
import logging

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
MONGO_HOST = os.getenv('MONGO_HOST', 'mongo')
MONGO_PORT = 27017
MONGO_USER = os.getenv('MONGO_USER', 'root')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'root')
MONGO_DB = os.getenv('MONGO_DB', 'code-challenge')

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG if ENVIRONMENT == 'development' else logging.INFO)
