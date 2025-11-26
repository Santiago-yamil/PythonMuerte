from sqlalchemy import Column, String
from app.models.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    rol = Column(String, nullable=False)  # ASPIRANTE, OPERADOR, EVALUADOR, ADMIN
