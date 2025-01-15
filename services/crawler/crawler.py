from exceptions import BadCrawlType
from .bs4crawler import BS4Crawler


class CrawlerService:
    def __init__(self, url, crawler):
        self.url = url
        self.crawler = crawler(url)

    async def crawl(self):
        await self.crawler.crawl()
        return self.crawler.url_contents


def crawl_builder(url, crawl_type):
    if crawl_type == "normal":
        return CrawlerService(url, BS4Crawler)
    raise BadCrawlType()

