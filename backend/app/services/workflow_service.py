# app/services/workflow_service.py

from sqlalchemy.orm import Session

from app.models.solicitud import Solicitud, EstadoSolicitud
from app.core.workflow import puede_transicionar, Rol


class WorkflowError(Exception):
    """Error para indicar problemas en el proceso de cambio de estado."""
    pass


def actualizar_estado_solicitud(db: Session, curp: str, rol: Rol, nuevo_estado: EstadoSolicitud) -> Solicitud:
    """
    Cambia el estado de una solicitud si el rol tiene permiso y la BD lo permite.
    """

    # 1. Buscar solicitud
    solicitud = db.query(Solicitud).filter(Solicitud.curp == curp).first()
    if not solicitud:
        raise WorkflowError(f"No existe la solicitud con CURP {curp}")

    estado_actual = solicitud.estado

    # 2. Validar transición usando el workflow
    if not puede_transicionar(rol, estado_actual, nuevo_estado):
        raise WorkflowError(
            f"El rol '{rol.name}' NO puede mover la solicitud de {estado_actual.value} → {nuevo_estado.value}"
        )

    # 3. Actualizar estado
    solicitud.estado = nuevo_estado

    # 4. Guardar cambios
    db.commit()
    db.refresh(solicitud)

    return solicitud


def obtener_transiciones_para_rol(rol: Rol, estado_actual: EstadoSolicitud):
    """
    Devuelve los posibles estados a los que el rol puede mover la solicitud.
    """

    from app.core.workflow import obtener_transiciones_posibles
    return obtener_transiciones_posibles(rol, estado_actual)
