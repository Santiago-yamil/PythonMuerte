from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship
from app.models.base import Base

class Apoyo(Base):
    __tablename__ = "apoyos"

    id = Column(String, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    desc = Column(Text, nullable=False)
    prerrequisitos = Column(Text, nullable=False)
    keywords = Column(Text, nullable=False)  # CSV simple
    tipo = Column(String, default="CURSO")
    capacidad = Column(Integer, default=10)

    # Relación inversa
    solicitudes = relationship("Solicitud", back_populates="apoyo")
