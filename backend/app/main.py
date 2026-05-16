from fastapi import FastAPI

from backend.app.api.v1.routes import router as v1_router
from backend.app.core.config import settings
from backend.app.core.logging import configure_logging

configure_logging(settings.log_level)

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(v1_router, prefix="/api/v1")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}
