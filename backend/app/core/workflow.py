from app.models.enums import Rol, EstadoSolicitud

WORKFLOW = {
    Rol.OPERADOR: {
        EstadoSolicitud.EN_CAPTURA: [EstadoSolicitud.ENVIADA],
        EstadoSolicitud.ENVIADA: [EstadoSolicitud.VALIDADA, EstadoSolicitud.RECHAZADA],
    },
    Rol.VALIDADOR: {
        EstadoSolicitud.ENVIADA: [EstadoSolicitud.VALIDADA, EstadoSolicitud.RECHAZADA],
        EstadoSolicitud.VALIDADA: [EstadoSolicitud.COMPLETADA],
    },
    Rol.ADMIN: {
        EstadoSolicitud.EN_CAPTURA: list(EstadoSolicitud),
        EstadoSolicitud.ENVIADA: list(EstadoSolicitud),
        EstadoSolicitud.VALIDADA: list(EstadoSolicitud),
        EstadoSolicitud.RECHAZADA: list(EstadoSolicitud),
        EstadoSolicitud.COMPLETADA: list(EstadoSolicitud),
    }
}

def puede_transicionar(rol: Rol, estado_actual: EstadoSolicitud, nuevo_estado: EstadoSolicitud) -> bool:
    return nuevo_estado in WORKFLOW.get(rol, {}).get(estado_actual, [])
