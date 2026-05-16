class TeamsClient:
    async def send_notification(self, channel: str, message: str) -> None:
        _ = (channel, message)
