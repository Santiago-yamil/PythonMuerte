#from pydantic import BaseSettings
#from pydantic_settings import BaseSettings
#from sqlalchemy import create_engine
#Remota============================================================================
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Cambia estos datos con los de tu servidor
DB_USER = "hacka_ito"
DB_PASSWORD = "hackaito2025"
DB_HOST = "172.32.5.67"  
DB_PORT = "5432"
DB_NAME = "hackatec"

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Función para obtener sesión (útil en Depends)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
