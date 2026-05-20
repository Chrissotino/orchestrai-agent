from datetime import datetime, timedelta, timezone

import pytest

from workflows.engines.follow_up_engine import FollowUpWorkflowEngine


@pytest.mark.asyncio
async def test_follow_up_wait() -> None:
    engine = FollowUpWorkflowEngine()
    recent = datetime.now(timezone.utc) - timedelta(hours=2)
    result = await engine.evaluate("t1", recent)
    assert result == "wait"


@pytest.mark.asyncio
async def test_follow_up_send_email() -> None:
    engine = FollowUpWorkflowEngine()
    stale = datetime.now(timezone.utc) - timedelta(hours=30)
    result = await engine.evaluate("t2", stale)
    assert result == "send_follow_up_email"


@pytest.mark.asyncio
async def test_follow_up_escalate_with_context() -> None:
    engine = FollowUpWorkflowEngine()
    stale = datetime.now(timezone.utc) - timedelta(hours=52)
    result = await engine.evaluate_with_context("t3", stale)
    assert result.next_action == "escalate_voice_or_manager"
    assert result.age_hours >= 52
    assert "escalation SLA" in result.rationale


def test_follow_up_engine_rejects_invalid_thresholds() -> None:
    with pytest.raises(ValueError):
        FollowUpWorkflowEngine(follow_up_after_hours=0)
    with pytest.raises(ValueError):
        FollowUpWorkflowEngine(follow_up_after_hours=24, escalate_after_hours=24)
