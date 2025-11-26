from pydantic import BaseModel
from app.core.workflow import Rol, EstadoSolicitud

class CambioEstadoRequest(BaseModel):
    curp: str
    rol: Rol
    nuevo_estado: EstadoSolicitud

    class Config:
        use_enum_values = True
