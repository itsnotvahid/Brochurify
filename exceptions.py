from fastapi import HTTPException
from fastapi import WebSocketException

class BadUrlException(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = ("There is something wrong with the url you provided,"
                       " please check and try again.")


class BadCrawlType(WebSocketException):
    def __init__(self):
        self.reason = "Bad TYPE BRO"
        self.code = 931

class BadContent(WebSocketException):
    def __init__(self):
        self.reason = "Bad Content, Try Again"
        self.code = 932
