from fastapi import APIRouter

from backend.app.schemas.workflow import WorkflowRequest, WorkflowResponse
from backend.app.services.email_orchestrator import EmailOrchestrator
from workflows.engines.follow_up_engine import FollowUpWorkflowEngine

router = APIRouter()
engine = FollowUpWorkflowEngine()
email_orchestrator = EmailOrchestrator()


@router.post("/orchestrate", response_model=WorkflowResponse)
async def orchestrate(request: WorkflowRequest) -> WorkflowResponse:
    decision = await email_orchestrator.intent_agent.analyze(request.email_body)
    next_action = await engine.evaluate(request.thread_id, request.last_reply_at)
    priority = "critical" if decision["urgency"] == "high" else "medium"
    return WorkflowResponse(
        status="queued",
        next_action=next_action,
        priority=priority,
        rationale=f"intent={decision['intent']}; urgency={decision['urgency']}",
    )
