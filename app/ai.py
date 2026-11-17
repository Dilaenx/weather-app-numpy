from openai import OpenAI, AsyncOpenAI
from app.config import settings

client = AsyncOpenAI(api_key=settings.openai_api_key)

async def call_model(text) -> str:
    response = await client.responses.create(
        model=settings.openai_model,
        input="Write a one-sentence bedtime story about a unicorn.",
    )

    print(response.output_text)

