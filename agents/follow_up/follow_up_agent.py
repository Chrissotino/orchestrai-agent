class FollowUpAgent:
    async def build_follow_up_message(self, thread_context: str) -> str:
        return f"Friendly follow-up regarding: {thread_context[:80]}"
