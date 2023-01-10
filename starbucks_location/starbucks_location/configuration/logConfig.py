
# -*-coding:utf-8-*-

# Log Level
# CRITICAL 50   A fatal error, indicating the program crashing
# ERROR    40   A severer problem, indicating program didn't execute some function successfully
# WARNING  30   [Default] Something unexpected happened, but program is still working as imagined
# INFO     20   Information, used to guarantee everything OK
# DEBUG    10   Detailed information, usually used to diagnose problems

import logging
from datetime import datetime
from logging.config import dictConfig
import logging
import os

'''
-----------------------------------static variables-----------------------------------------
'''
now = datetime.now()    # - timedelta(hours = 24)
log_time = now.strftime('%Y-%m-%d')

# root path of the whole project
base_path: str = os.path.dirname(os.path.dirname(__file__))
# path of the log file
log_path: str = os.path.join(base_path, 'log')
# name of the log file
log_name: str = [f"{log_time}.log", f"{log_time}ERR.log"]

# Format of different level of Logger
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s]: %(message)s'
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]: %(message)s'
compact_format = '[%(levelname)s][%(asctime)s]: %(message)s'

# Sophisticated Logging comfiguration
dic_conf = {
    'version': 1,
    # Disable any Logger that already exists
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format,
            'datefmt' : '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': simple_format,
            'datefmt' : '%Y-%m-%d %H:%M:%S'
        },
        'compact': {
            'format': compact_format,
            'datefmt' : '%Y-%m-%d %H:%M:%S'
        },
    },
    # Filter
    'filters': {},
    'handlers': {
        # Logging that prints at files, including at least INFO level
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': f"{log_path}\{log_name[0]}",
            'maxBytes': 1024*1024*5,  # Size of log file: 5M
            'backupCount': 5,
            'encoding': 'utf-8',
        },
        # Logging that prints at console
        'stream': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # Logging that prings at files, including at least ERROR level
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': f'{log_path}\{log_name[1]}',
            'maxBytes': 1024*1024*5,  # Size of log file: 5M
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    # Logger
    'loggers': {
        # Default Logger configuration that used by logging.getLogger(__name__)
        '': {
            'handlers': ['stream', 'default', 'error'],
            'level': 'DEBUG',
            # Pass info up to higher level Loggers, default: True
            'propagate': False,
        },
        # Other Logger configuration
        'l_error': {
            'handlers': ['error',],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}


'''
------------------------------------------functions--------------------------------
'''
def initLogger(name: str) -> logging.Logger:
    # Set the configuration to Logger
    dictConfig(dic_conf)
    # Generate the configured Logger
    logger = logging.getLogger(name)
    # Record the running statement of Logger
    logger.info('Logger configuring finished.')
    return logger


'''
------------------------------------------main---------------------------------------
'''
if __name__ == '__main__':
    initLogger()
    pass