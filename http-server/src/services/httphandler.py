import os
import mimetypes

class HTTPHandler:

    def HTTP_501_handler(self, request):
        response_line = self.response_line(status_code=self.HTTP_NOT_IMPLEMENTED_CODE)

        response_headers = self.response_headers()

        blank_line = self.BLANK_LINE

        response_body = self.NOT_IMPLEMENTED_BODY 

        return "%s%s%s%s" % (
                response_line, 
                response_headers, 
                blank_line, 
                response_body
            )

    def handle_OPTIONS(self, request):
        response_line = self.response_line(self.HTTP_OK_CODE)

        response_headers = self.response_headers(self.EXTRA_HEADERS)

        blank_line = self.BLANK_LINE

        return "%s%s%s" % (
                response_line, 
                response_headers,
                blank_line
            )

    def handle_GET(self, request):
        filename = request.uri.strip('/') # remove the slash from URI

        if filename is not None and os.path.exists('views/'+filename):
            response_line = self.response_line(self.HTTP_OK_CODE)

             # find out a file's MIME type
            # if nothing is found, just send `text/html`
            content_type = mimetypes.guess_type(filename)[0] or 'text/html'

            extra_headers = {'Content-Type': content_type}
            response_headers = self.response_headers(extra_headers)

            with open('views/'+filename) as f:
                response_body = f.read()
        else:
            response_line = self.response_line(self.HTTP_NOT_FOUND_CODE)
            response_headers = self.response_headers()
            response_body = self.NOT_FOUND_BODY

        blank_line = self.BLANK_LINE

        return "%s%s%s%s" % (
                response_line, 
                response_headers, 
                blank_line, 
                response_body
            )