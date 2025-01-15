from .open_ai import OpenAIModel
class LLMService:
    def __init__(self, llm):
        self.llm = OpenAIModel()

    async def generate_response(self, crawl_result):
        async for response_chunk in self.llm.generate(crawl_result):
            yield response_chunk
