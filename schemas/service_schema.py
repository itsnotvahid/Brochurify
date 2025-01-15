from pydantic import BaseModel


class WebSiteSchema(BaseModel):
    url: str
    site_type: str = ""
    additional_description: str = ""

