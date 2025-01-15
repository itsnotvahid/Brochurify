from fastapi import APIRouter

from schemas import WebSiteSchema
from services.crawler import CrawlerService, BS4Crawler
router = APIRouter()


@router.post("/get_brochure")
async def get_brochure(website: WebSiteSchema):
    cr_service = CrawlerService(website.url, BS4Crawler)
    data = await cr_service.crawl()
    return {"data": data}
