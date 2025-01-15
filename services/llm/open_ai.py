from openai import AsyncOpenAI

with open("services/llm/api-key", "r") as f:
    api_key = f.read()


class OpenAIModel:
    def __init__(self):
        self.api_key = api_key
        self.model = "GPT-4O-mini"
        self.openai = AsyncOpenAI(api_key=api_key)

    async def generate(self, prompt):
        response = await self.openai.chat.completions.create(model="gpt-4o-mini",
                                                             messages=prompt, stream=True)
        async for response_chunk in response:
            yield response_chunk.choices[0].delta.content

