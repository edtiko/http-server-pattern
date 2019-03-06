# main.py 
from services.httpserver import HTTPServer

if __name__ == '__main__':
    server = HTTPServer()
    server.start()