from services.socket import ConnectionManager


class Orchestrator:
    def __init__(self, crawler_service, llm_service):
        self.crawler_service = crawler_service
        self.llm_service = llm_service

    async def stream_website_data(self, user_id: str, manager: ConnectionManager):

        await manager.send_message(user_id, "Starting crawling process...")
        crawl_result = await self.crawler_service.crawl()
        yield f"Crawling completed. Extracted content: {crawl_result[:200]}..."

        crawl_result = [
            {"role": "user", "content": "hey just write me 50 tokens randomly and talk about god"},
            {"role": "system", "content": "You are an assistant to superman "}
        ]
        await manager.send_message(user_id, "Processing content with LLM...")
        async for llm_update in self.llm_service.generate_response(
            crawl_result=crawl_result
        ):
            yield llm_update
