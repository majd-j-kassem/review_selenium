"""
Logger Demo
"""
import logging
import logging.config 

class LoggerDemoConfig():

    def testLog(self):
        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConfig.__name__)

        # create console handler and set level to info
       
        # create formatter
       
        # add formatter to console handler
       
        # add console handler to logger
        

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConfig()
demo.testLog()