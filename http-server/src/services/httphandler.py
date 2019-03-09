import os
import mimetypes
from util.httpconstant import HTTPConstant
from services.httpresponse import HTTPResponse

class HTTPHandler(HTTPConstant):

    def __init__(self, method):
        self.handler = None
        self.resolve_handler(method)

    def resolve_handler(self, method):
        try:
            self.handler = getattr(self, 'handle_%s' % method)
        except AttributeError:
            self.handler = self.handle_ERROR

    def handle_ERROR(self, request):
        http_response = HTTPResponse(self.HTTP_NOT_IMPLEMENTED_CODE, None, self.NOT_IMPLEMENTED_BODY)

        return http_response.build()


    def handle_OPTIONS(self, request):

        http_response = HTTPResponse(self.HTTP_OK_CODE, self.EXTRA_HEADERS, self.HTTP_OPTIONS_BODY)
        
        return http_response.build()

    def handle_GET(self, request):
        filename = request.uri.strip('/') # remove the slash from URI

        if filename is not '' and filename is not None and os.path.exists(self.PATH_VIEWS+filename):
            status_code = self.HTTP_OK_CODE

            # find out a file's MIME type
            # if nothing is found, just send `text/html`
            content_type = mimetypes.guess_type(filename)[0] or self.CONTENT_TYPE_TEXT_HTML

            extra_headers = {'Content-Type': content_type}

            with open(self.PATH_VIEWS+filename) as f:
                body = f.read()
        else:
            status_code = self.HTTP_NOT_FOUND_CODE
            extra_headers = None
            body = self.NOT_FOUND_BODY
        
        http_response = HTTPResponse(status_code, extra_headers, body)
        
        return http_response.build()

    def handle_POST(self, request):
        http_response = HTTPResponse(self.HTTP_OK_CODE, None, self.HTTP_POST_BODY)
        
        return http_response.build()
    
    def handle_PUT(self, request):
        http_response = HTTPResponse(self.HTTP_OK_CODE, None, self.HTTP_PUT_BODY)
        
        return http_response.build()
    
    def handle_DELETE(self, request):
        http_response = HTTPResponse(self.HTTP_OK_CODE, None, self.HTTP_DELETE_BODY)
        
        return http_response.build()
    
    def handle_PATCH(self, request):
        http_response = HTTPResponse(self.HTTP_OK_CODE, None, self.HTTP_PATCH_BODY)
        
        return http_response.build()