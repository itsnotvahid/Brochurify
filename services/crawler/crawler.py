

class CrawlerService:
    def __init__(self, url, crawler):
        self.url = url
        self.crawler = crawler(url)

    async def crawl(self):
        await self.crawler.crawl()
        return self.crawler.url_contents
