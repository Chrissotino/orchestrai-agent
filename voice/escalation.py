class VoiceEscalationService:
    async def trigger_call(self, to_number: str, reason: str) -> dict:
        # Twilio / Vapi integration placeholder.
        return {"destination": to_number, "reason": reason, "status": "initiated"}
