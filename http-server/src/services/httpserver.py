from services.tcpserver import TCPServer
from services.httprequest import HTTPRequest
from services.httphandler import HTTPHandler

class HTTPServer(TCPServer, HTTPHandler):

    #handle data request
    def handle_request(self, data):
        request = HTTPRequest(data)
        try:
            handler = getattr(self, 'handle_%s' % request.method)
        except AttributeError:
            handler = self.HTTP_501_handler

        response = handler(request)

        return response
    
    # return Http status
    def response_line(self, status_code):
        reason = self.STATUS_CODES[status_code]
        return "HTTP/1.1 %s %s\r\n" % (status_code, reason)

    # return Http headers
    def response_headers(self, extra_headers=None):
        headers_copy = self.HEADERS.copy() # make a local copy of headers

        if extra_headers:
            headers_copy.update(extra_headers)

        headers = ""

        for h in headers_copy:
            headers += "%s: %s\r\n" % (h, headers_copy[h])
        return headers

    