# main.py 
from services.httpserver import HTTPServer

if __name__ == '__main__':
    server = HTTPServer('127.0.0.1',8888)
    server.init_server()