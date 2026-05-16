class SharePointClient:
    async def upload_note(self, title: str, body: str) -> dict:
        return {"title": title, "saved": True}
