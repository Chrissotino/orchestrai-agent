class ExecutiveCoordinator:
    async def escalate_if_unconfirmed(self, workflow_id: str) -> dict:
        return {"workflow_id": workflow_id, "escalated": True, "channel": "voice"}
