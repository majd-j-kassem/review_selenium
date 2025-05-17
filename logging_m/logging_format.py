import logging


logging.basicConfig(format='%(asctime)s: %(levelname)s:  %(message)s',datefmt='%m/%d/%Y %I:%M:%s',
                    level=logging.DEBUG)

logging.debug('This is a debug message. It\'s very detailed.')
logging.info('This is an informational message.')
logging.warning('Something might be going wrong here.')
logging.error('An error occurred!')
logging.critical('System failure imminent!')