class HTTPConstant:

    HTTP_OK_CODE = 200
    HTTP_NOT_IMPLEMENTED_CODE = 501
    HTTP_NOT_FOUND_CODE = 404
    HEADERS = {
        'Server': 'CrudeServer',
        'Content-Type': 'text/html',
    }
    STATUS_CODES = {
        200: 'OK',
        404: 'Not Found',
        501: 'Not Implemented',
    }
    EXTRA_HEADERS = {'Allow': 'OPTIONS, GET, POST, PUT, DELETE, PATCH'}
    NOT_IMPLEMENTED_BODY = "<h1>501 Not Implemented</h1>"
    NOT_FOUND_BODY = "<h1>404 Not Found</h1>"
    HTTP_POST_BODY = "<h1>This is a POST Request</h1>"
    HTTP_PUT_BODY = "<h1>This is a PUT Request</h1>"
    HTTP_DELETE_BODY = "<h1>This is a DELETE Request</h1>"
    HTTP_PATCH_BODY = "<h1>This is a PATCH Request</h1>"
    HTTP_OPTIONS_BODY = "<h1>This is a OPTIONS Request</h1>"
    BLANK_LINE = "\r\n"
    CONTENT_TYPE_TEXT_HTML = "text/html"
    PATH_VIEWS = "views/"