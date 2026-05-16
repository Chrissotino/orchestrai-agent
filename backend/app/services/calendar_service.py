from integrations.microsoft365.calendar_client import Microsoft365CalendarClient


class CalendarService:
    def __init__(self) -> None:
        self.client = Microsoft365CalendarClient()

    async def create_colleague_event(self, owner: str, title: str, start: str, end: str) -> dict:
        return await self.client.create_event(owner=owner, title=title, start=start, end=end)
