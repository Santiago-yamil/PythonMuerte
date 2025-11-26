from enum import Enum

class Rol(Enum):
    OPERADOR = "OPERADOR"
    VALIDADOR = "VALIDADOR"
    ADMIN = "ADMIN"

class EstadoSolicitud(Enum):
    EN_CAPTURA = "EN_CAPTURA"
    ENVIADA = "ENVIADA"          # NECESARIO PARA EL WORKFLOW
    VALIDADA = "VALIDADA"
    RECHAZADA = "RECHAZADA"
    COMPLETADA = "COMPLETADA"
