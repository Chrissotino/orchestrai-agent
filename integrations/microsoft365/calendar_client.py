class Microsoft365CalendarClient:
    async def create_event(self, owner: str, title: str, start: str, end: str) -> dict:
        return {"owner": owner, "title": title, "start": start, "end": end, "status": "created"}
