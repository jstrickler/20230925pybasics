import logging

logging.basicConfig(
    filename='../LOGS/simple.log',
    level=logging.WARNING,
)

logger = logging.getLogger()

logger.warning('This is a warning') # message will be output
logger.debug('This message is for debugging') # message will NOT be output
logger.error('This is an ERROR') # message will be output
logger.critical('This is ***CRITICAL***') # message will be output
logger.info('The capital of North Dakota is Bismark') # message will not be output

