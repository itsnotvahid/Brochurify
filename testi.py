import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def show_status(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://google.com/", "https://howsam.org",
                "https://www.google.com/search?q=python",
                "https://www.google.com/search?q=sex", "max_mn.t",
               ]

        requests = [show_status(session, url) for url in urls]
        responses = await asyncio.gather(*requests, return_exceptions=True)
        # response = await show_status(session, url)
        # print(responses[0])
        soups = [BeautifulSoup(response, 'html.parser') for response in responses
                 if not isinstance(response, BaseException)]
        for soup in soups:
            print(soup.title.string)

if __name__ == '__main__':
    asyncio.run(main())