class ClientException(IOError):
    def __init__(self, code, message, *args, **kwargs):
        self.code = code
        self.message = message
        super(ClientException, self).__init__(args, kwargs)
