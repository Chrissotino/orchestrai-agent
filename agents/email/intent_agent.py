from backend.app.services.openai_service import OpenAIService


class EmailIntentAgent:
    def __init__(self) -> None:
        self.ai = OpenAIService()

    async def analyze(self, email_body: str) -> dict[str, str]:
        summary = await self.ai.summarize_intent(email_body)
        lowered = summary.lower()
        intent = "schedule" if "meeting" in lowered or "schedule" in lowered else "reply"
        urgency = "high" if any(token in lowered for token in ["urgent", "asap", "today"]) else "normal"
        return {"summary": summary, "intent": intent, "urgency": urgency}
