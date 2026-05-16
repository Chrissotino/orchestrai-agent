from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "development"
    app_name: str = "OrchestrAI Agent"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "INFO"

    openai_api_key: str = ""
    openai_model: str = "gpt-4.1"

    mcp_server_url: str = "http://localhost:9000"
    mcp_api_key: str = ""


settings = Settings()
