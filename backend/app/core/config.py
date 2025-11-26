from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Plataforma Integral"
    OCR_PROVIDER: str = "tesseract"
    AI_MODEL: str = "modelo_validacion_v1"
    DATABASE_URL: str = "sqlite:///./database.db"

    class Config:
        env_file = ".env"

settings = Settings()
