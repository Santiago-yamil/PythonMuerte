from sqlalchemy import Column, String, Integer, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.enums import EstadoSolicitud


class Solicitud(Base):
    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True, index=True)

    curp = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    primerApellido = Column(String, nullable=False)
    ineUrl = Column(String, nullable=False)
    cvUrl = Column(String, nullable=False)
    apoyo_id = Column(String, ForeignKey("apoyos.id"), nullable=False)

    # 👉 ESTE ES EL CAMPO QUE TE DECÍA
    estado = Column(Enum(EstadoSolicitud), default=EstadoSolicitud.EN_CAPTURA)

    # Relaciones opcionales
    apoyo = relationship("Apoyo", back_populates="solicitudes")
