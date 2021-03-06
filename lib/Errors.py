class Error(Exception):
    def __init__(self, http_status_code, http_message, internal_code, internal_message):
        self.http_status_code = http_status_code
        self.http_message = http_message
        self.internal_code = internal_code
        self.internal_message = internal_message

    def http_error(self):
        return self.http_message, self.http_status_code


XML_FILE_INVALID = Error(400, 'File invalid', 1111, 'Xml file invalid')
DATA_CONTAINER_TYPE_INVALID = Error(500, 'Server internal error', 2222, 'DATA_CONTAINER_TYPE_INVALID')
UPDATE_TRACK_DATA_INVALID = Error(400, 'Data invalid', 3333, 'Info in request invalid')
DATA_NOT_FOUND = Error(401, 'Data not found', 3333, 'Data not found')

LOGIN_REQUIRED = Error(401, 'Please login', 4444, 'Login required')
