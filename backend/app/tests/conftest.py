import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
import sys
import os
from app.models.solicitud import Solicitud, EstadoSolicitud
from app.models.enums import Rol
from app.services.workflow_service import actualizar_estado_solicitud

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, BASE_DIR)


@pytest.fixture
def db_session():
    # Base de datos temporal en memoria SOLO PARA TESTS
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Crear tablas
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
