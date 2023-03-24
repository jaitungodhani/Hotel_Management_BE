class ResponseMsg:
    def __init__(self, data, error, message):
        self.data = data
        self.error = error
        self.message = message

        self.response = {
            'error':self.error,
            'data':self.data,
            'message':self.message
        }

