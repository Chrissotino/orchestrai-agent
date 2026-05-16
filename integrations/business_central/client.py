class BusinessCentralClient:
    async def create_task(self, payload: dict) -> dict:
        return {"status": "queued", "payload": payload}
