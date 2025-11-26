from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime
from app.models.base import Base

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(String, primary_key=True)
    tipo = Column(String, nullable=False)       # INE, CV, etc.
    url = Column(String, nullable=False)
    validado = Column(String, default="NO")     # "SI" / "NO"
    fecha_subida = Column(DateTime, default=datetime.utcnow)
