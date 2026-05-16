from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class WorkflowRequest(BaseModel):
    thread_id: str = Field(..., description="Unique thread identifier")
    last_reply_at: datetime = Field(..., description="Timestamp of last outbound or inbound reply")
    email_body: str = Field(..., min_length=3, description="Latest thread content")


class WorkflowResponse(BaseModel):
    status: Literal["queued", "completed"]
    next_action: str
    priority: Literal["low", "medium", "high", "critical"]
    rationale: str
