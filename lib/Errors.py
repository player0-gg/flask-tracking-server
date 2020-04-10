class Error(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


XML_ROOT_INVALID = Error(500, "File invalid")
