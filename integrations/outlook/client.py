class OutlookClient:
    async def fetch_email(self, email_id: str) -> dict:
        return {"id": email_id, "subject": "Placeholder", "body": "Please schedule leadership sync."}
