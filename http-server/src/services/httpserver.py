from services.tcpserver import TCPServer
from services.httprequest import HTTPRequest
from services.httphandler import HTTPHandler
from services.httplogging import HTTPLogging

class HTTPServer():

    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    def init_server(self):
        tcp = TCPServer(self.host, self.port)
        tcp.start(self.handle_request)

    def handle_request(self, data):
        request = HTTPRequest(data)
        self.write_request_log(data)
        http_handler = HTTPHandler(request.method)  
        #get http response         
        response = http_handler.handler(request)

        return response

    def write_request_log(self, data):
        logging = HTTPLogging()
        logging.writeLog(data)
