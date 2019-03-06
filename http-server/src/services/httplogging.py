import logging

class HTTPLogging:
    def __init__(self, filename='http_request.log'):
        self.filename = filename
        logging.basicConfig(filename=filename,level=logging.INFO)


    def writeLog(self, data):
        logging.info(data)