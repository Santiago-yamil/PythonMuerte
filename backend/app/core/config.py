#from pydantic import BaseSettings
from pydantic_settings import BaseSettings
from sqlalchemy import create_engine

class Settings(BaseSettings):
    APP_NAME: str = "Plataforma Integral"
    OCR_PROVIDER: str = "tesseract"
    AI_MODEL: str = "modelo_validacion_v1"
    DATABASE_URL: str = "sqlite:///./database.db"

    class Config:
        env_file = ".env"

settings = Settings()
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Motor y sesión de SQLAlchemy
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


settings = Settings()
from app.models.solicitud import Solicitud
from app.models.apoyo import Apoyo
# Importa aquí otros modelos si los hay

Base.metadata.create_all(bind=engine)
