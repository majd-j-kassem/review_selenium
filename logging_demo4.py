import logging 
import custom_logger as cl 

class LogoDemo4():
    logger = cl.custom_logger(logging.DEBUG)
    
    def method1(self):
        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warning('warn message')
        self.logger.error('error message')
        self.logger.critical('critical message')
    def method2(self):
        method_2_log = cl.custom_logger(logging_level=logging.DEBUG)
        method_2_log.debug('debug message')
        method_2_log.info('info message')
        method_2_log.warning('warn message')
        method_2_log.error('error message')
        method_2_log.critical('critical message')
    def method3(self):
        self.logger.debug('debug message')
        self.logger.info('info message')
        self.logger.warning('warn message')
        self.logger.error('error message')
        self.logger.critical('critical message')
demo = LogoDemo4()
demo.method1()
demo.method2()
demo.method3()