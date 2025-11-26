# backend/app/api/v1/schemas/workflow_schemas.py

    #Por si falla descomentar
#from app.models.enums import Rol, EstadoSolicitud

from pydantic import BaseModel
from typing import Literal
# Importamos los Enums que definieron en el core del workflow
# Si en tu proyecto tienes los enums en otro sitio (por ejemplo app.models.enums)
# cambia la importación por la ruta correcta.
from app.core.workflow import Rol, EstadoSolicitud


class CambioEstadoRequest(BaseModel):
    curp: str
    rol: Rol
    nuevo_estado: EstadoSolicitud

    class Config:
        use_enum_values = True  # serialize enums por su valor string
