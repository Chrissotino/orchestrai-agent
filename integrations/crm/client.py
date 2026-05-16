class CRMClient:
    async def create_activity(self, account_id: str, summary: str) -> dict:
        return {"account_id": account_id, "summary": summary, "status": "created"}
