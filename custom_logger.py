import logging
import inspect # You'll need to import this module for inspect.stack()

def custom_logger(logging_level):
    # 1. Dynamically get the name of the calling function
    logger_name = inspect.stack()[1][3]

    # 2. Get (or create) a logger instance with that name
    logger = logging.getLogger(logger_name)

    # 3. Set the logger's overall processing level
    logger.setLevel(logging.DEBUG)

    # 4. Create a FileHandler
    #    It will write to a file named after the logger (and thus, the calling function)
    #    'mode="w"' means the file will be overwritten each time the handler is created
    file_handeler = logging.FileHandler('{0}.log'.format(logger_name), mode='w')

    # 5. Set the FileHandler's specific logging level
    file_handeler.setLevel(logging_level)

    # 6. Create a Formatter to define the log message layout
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

    # 7. Attach the formatter to the file handler
    file_handeler.setFormatter(formatter)