from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Auditoria(Base):
    __tablename__ = "auditoria"

    id = Column(String, primary_key=True)  # puede ser un UUID
    curp = Column(String, nullable=False)
    rol = Column(String, nullable=False)
    estado_anterior = Column(String, nullable=False)
    estado_nuevo = Column(String, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
