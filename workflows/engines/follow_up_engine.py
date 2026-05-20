from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(slots=True)
class FollowUpDecision:
    next_action: str
    age_hours: float
    rationale: str


class FollowUpWorkflowEngine:
    def __init__(
        self,
        *,
        follow_up_after_hours: int = 24,
        escalate_after_hours: int = 48,
    ) -> None:
        if follow_up_after_hours <= 0:
            raise ValueError("follow_up_after_hours must be positive")
        if escalate_after_hours <= follow_up_after_hours:
            raise ValueError("escalate_after_hours must be greater than follow_up_after_hours")
        self.follow_up_after_hours = follow_up_after_hours
        self.escalate_after_hours = escalate_after_hours

    async def evaluate(self, thread_id: str, last_reply_at: datetime) -> str:
        decision = await self.evaluate_with_context(thread_id, last_reply_at)
        return decision.next_action

    async def evaluate_with_context(self, thread_id: str, last_reply_at: datetime) -> FollowUpDecision:
        _ = thread_id
        age_hours = (datetime.now(timezone.utc) - last_reply_at).total_seconds() / 3600
        if age_hours >= self.escalate_after_hours:
            return FollowUpDecision(
                next_action="escalate_voice_or_manager",
                age_hours=age_hours,
                rationale=(
                    f"Thread idle for {age_hours:.1f}h (>= {self.escalate_after_hours}h escalation SLA)."
                ),
            )
        if age_hours >= self.follow_up_after_hours:
            return FollowUpDecision(
                next_action="send_follow_up_email",
                age_hours=age_hours,
                rationale=f"Thread idle for {age_hours:.1f}h (>= {self.follow_up_after_hours}h follow-up SLA).",
            )
        return FollowUpDecision(
            next_action="wait",
            age_hours=age_hours,
            rationale=f"Thread idle for {age_hours:.1f}h (< {self.follow_up_after_hours}h follow-up SLA).",
        )
