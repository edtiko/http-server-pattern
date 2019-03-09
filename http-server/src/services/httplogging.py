import logging

class HTTPLogging:
    def __init__(self, filename='http_request.log'):
        self.filename = filename
        logging.basicConfig(filename=filename,level=logging.INFO, format='%(asctime)s;%(levelname)s;%(message)s',
         datefmt='%Y-%m-%d %H:%M:%S')


    def writeLog(self, data):
        logging.info(data)