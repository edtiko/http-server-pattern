class Util:

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
    EXTRA_HEADERS = {'Allow': 'OPTIONS, GET'}
    NOT_IMPLEMENTED_BODY = "<h1>501 Not Implemented</h1>"
    NOT_FOUND_BODY = "<h1>404 Not Found</h1>"
    BLANK_LINE = "\r\n"