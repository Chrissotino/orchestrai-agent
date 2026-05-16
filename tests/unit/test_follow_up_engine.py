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
