from fastapi import HTTPException


class BadUrlException(HTTPException):
    def __init__(self):
        self.status_code = 400
        self.detail = ("There is something wrong with the url you provided,"
                       " please check and try again.")

