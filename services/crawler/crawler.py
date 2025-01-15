import asyncio
import aiohttp
from bs4 import BeautifulSoup

from exceptions import BadUrlException
from dataclasses import dataclass


@dataclass
class URLContent:
    def __init__(self, url, content):
        self.url = url
        self.content = content


class BS4Crawler:
    def __init__(self, url):
        self.url = url
        self.visited_links = list()
        self.url_contents = list()

    @staticmethod
    async def _fetch(session, link):
        async with session.get(link) as response:
            return await response.text(return_exceptions=True)

    @staticmethod
    def get_soup_content(soup):
        title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            text = title + "\t" + soup.body.get_text(separator="\n", strip=True)
            return text
        return ""

    async def main_page_crawl(self, session):
        response = await self._fetch(session, self.url)
        if isinstance(response, BaseException):
            raise BadUrlException()
        soup = BeautifulSoup(response, 'html.parser')

        main_page_text = self.get_soup_content(soup)
        return main_page_text, soup

    @staticmethod
    async def crawl(self):
        async with aiohttp.ClientSession() as session:
            main_page_text, soup = await self.main_page_crawl(session)
            self.url_contents.append(URLContent(self.url, main_page_text))
            self.visited_links.append(self.url)
            links = [link.get('href') for link in soup.find_all('a')]

            requests = list()
            for link in links:
                if link not in self.visited_links:
                    requests.append(self.get_url_content(session, link))
                    self.visited_links.append(link)
            if requests:
                responses = await asyncio.gather(*requests, return_exceptions=True)
                for response in responses:
                    if response:
                        self.url_contents.append(response)

    async def get_url_content(self, session, link):
        response = await self._fetch(session, link)
        if isinstance(response, BaseException):
            return None
        soup = BeautifulSoup(response, 'html.parser')
        text = self.get_soup_content(soup)
        return URLContent(link, text)


class CrawlerService:
    def __init__(self, url, crawler):
        self.url = url
        self.crawler = crawler

    async def crawl(self):
        await self.crawler.crawl()
        return self.crawler.url_contents
