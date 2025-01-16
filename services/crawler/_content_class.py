from dataclasses import dataclass
from pydantic import BaseModel

# @dataclass
class URLContent(BaseModel):
    url: str
    content: str

