from openai import AsyncOpenAI

from backend.app.core.config import settings


class OpenAIService:
    def __init__(self) -> None:
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    async def summarize_intent(self, email_text: str) -> str:
        if not settings.openai_api_key:
            return "No API key configured; fallback analysis path in use."

        response = await self.client.responses.create(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": "Extract concise intent and urgency markers for enterprise email orchestration.",
                },
                {"role": "user", "content": email_text},
            ],
        )
        return response.output_text
