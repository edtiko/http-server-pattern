from util.httpconstant import HTTPConstant

class HTTPResponse(HTTPConstant):

    def __init__(self, status_code, extra_headers=None, body=None):
        self.status_code = status_code
        self.extra_headers = extra_headers
        self.body = body

    def build(self):
        response_line = self.response_line()
        response_headers = self.response_headers()
        blank_line = self.BLANK_LINE
        response_body = self.body

        return "%s%s%s%s" % (
                response_line, 
                response_headers, 
                blank_line, 
                response_body
            )   

    # return Http status
    def response_line(self):
        reason = self.STATUS_CODES[self.status_code]
        return "HTTP/1.1 %s %s\r\n" % (self.status_code, reason)

    # return Http headers
    def response_headers(self):
        headers_copy = self.HEADERS.copy() # make a local copy of headers

        if self.extra_headers:
            headers_copy.update(self.extra_headers)

        headers = ""

        for h in headers_copy:
            headers += "%s: %s\r\n" % (h, headers_copy[h])
        return headers        