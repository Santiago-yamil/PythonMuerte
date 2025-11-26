from app.services.workflow_service import actualizar_estado_solicitud, WorkflowError
from app.core.workflow import Rol
from app.models.solicitud import Solicitud, EstadoSolicitud


def test_operador_valida_solicitud(db_session):
    # Crear solicitud inicial
    solicitud = Solicitud(
        curp="ABC123",
        nombre="Juan",
        primerApellido="Pérez",
        ineUrl="url",
        cvUrl="url",
        apoyo_id="APOYO1"
    )
    db_session.add(solicitud)
    db_session.commit()

    # Cambiar estado como OPERADOR
    actualizada = actualizar_estado_solicitud(
        db=db_session,
        curp="ABC123",
        rol=Rol.OPERADOR,
        nuevo_estado=EstadoSolicitud.VALIDADA
    )

    assert actualizada.estado == EstadoSolicitud.VALIDADA
