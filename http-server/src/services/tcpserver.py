import socket
from util.httpconstant import HTTPConstant

class TCPServer(HTTPConstant):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self, handle):
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
          self.request_resolve(s, handle)
   
    def request_resolve(self, socket, handle):
        # accept any new connection
        conn, addr = socket.accept()

        print("Connected by", addr)

        # read the data sent by the client (1024 bytes)
        data = conn.recv(1024)

        # handle request on http server
        response = handle(data)

        conn.sendall(response.encode('utf-8'))
        conn.close()
