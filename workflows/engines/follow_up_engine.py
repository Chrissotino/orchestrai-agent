from datetime import datetime, timezone


class FollowUpWorkflowEngine:
    async def evaluate(self, thread_id: str, last_reply_at: datetime) -> str:
        _ = thread_id
        age_hours = (datetime.now(timezone.utc) - last_reply_at).total_seconds() / 3600
        if age_hours >= 48:
            return "escalate_voice_or_manager"
        if age_hours >= 24:
            return "send_follow_up_email"
        return "wait"
