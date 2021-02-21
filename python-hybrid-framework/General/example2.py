import logging

# If you run the above script several times,
# the messages from successive runs are appended to the file
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# If you want each run to start afresh, not remembering the messages from earlier runs,
# you can specify the filemode argument
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, filemode='w')

logging.debug('Logging.Debug')
logging.info('Logging: Info')
logging.warning('Logging: Warning')
logging.error('Logging: Error')
