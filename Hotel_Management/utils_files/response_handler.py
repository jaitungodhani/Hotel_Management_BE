
class ResponseMsg:
    def __init__(self,data,error,msg):
        self.data=data
        self.error=error
        self.msg=msg
        self.response={
        'error':self.error,
        'data': self.data,
        'message': self.msg
    }
    

    