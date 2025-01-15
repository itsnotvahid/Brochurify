from fastapi import HTTPException
from fastapi import WebSocketException

class BadUrlException(WebSocketException):
    def __init__(self):
        self.code = 1000
        self.reason = "There is something wrong with the url you provided,\
                        please check and try again."


class BadCrawlType(WebSocketException):
    def __init__(self):
        self.reason = "Bad TYPE BRO"
        self.code = 1000

class BadContent(WebSocketException):
    def __init__(self):
        self.reason = "Bad Content, Try Again"
        self.code = 1000
