from backend.app.models.domain import OrchestrationDecision
from agents.email.intent_agent import EmailIntentAgent
from integrations.outlook.client import OutlookClient


class EmailOrchestrator:
    def __init__(self) -> None:
        self.intent_agent = EmailIntentAgent()
        self.outlook_client = OutlookClient()

    async def process_inbox_email(self, email_id: str) -> OrchestrationDecision:
        email = await self.outlook_client.fetch_email(email_id)
        analysis = await self.intent_agent.analyze(email["body"])
        priority = "critical" if analysis["urgency"] == "high" else "medium"
        action = "calendar_coordination" if analysis["intent"] == "schedule" else "draft_reply"
        return OrchestrationDecision(
            thread_id=email_id,
            priority=priority,
            action=action,
            rationale=f"Intent={analysis['intent']} urgency={analysis['urgency']}",
        )
