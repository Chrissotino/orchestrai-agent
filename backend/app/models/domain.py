from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class EmailThread:
    thread_id: str
    subject: str
    body: str
    sender: str
    received_at: datetime


@dataclass(slots=True)
class OrchestrationDecision:
    thread_id: str
    priority: str
    action: str
    rationale: str
