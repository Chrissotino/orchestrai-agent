class MCPClient:
    async def invoke_tool(self, tool_name: str, payload: dict) -> dict:
        return {"tool": tool_name, "payload": payload, "status": "mocked"}
