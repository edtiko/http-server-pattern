import socket
from services.httplogging import HTTPLogging
from util.util import Util

class TCPServer(Util):

    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    def start(self):
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket object to the address and port
        s.bind((self.host, self.port))
        # start listening for connections
        s.listen(5)

        print("Listening at", s.getsockname())
        #loop listens http requests
        while True:
          self.request_resolve(s)
   
    def request_resolve(self, socket):
        # accept any new connection
        conn, addr = socket.accept()

        print("Connected by", addr)

        # read the data sent by the client (1024 bytes)
        data = conn.recv(1024)

        # write request log
        self.write_request_log(data)

        # handle request on http server
        response = self.handle_request(data)

        conn.sendall(response.encode('utf-8'))
        conn.close()
    
    def write_request_log(self, data):
        logging = HTTPLogging()
        logging.writeLog(data)
