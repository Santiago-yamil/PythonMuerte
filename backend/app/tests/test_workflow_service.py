from app.models.solicitud import Solicitud, EstadoSolicitud
from app.services.workflow_service import actualizar_estado_solicitud, WorkflowError
from app.core.workflow import Rol


def test_operador_valida_solicitud(db_session):
    # Crear solicitud en EN_CAPTURA
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

    # Primero OPERADOR debe ENVIARLA
    solicitud = actualizar_estado_solicitud(
        db=db_session,
        curp="ABC123",
        rol=Rol.OPERADOR,
        nuevo_estado=EstadoSolicitud.ENVIADA
    )

    assert solicitud.estado == EstadoSolicitud.ENVIADA

    # Ahora SÍ puede validar
    solicitud = actualizar_estado_solicitud(
        db=db_session,
        curp="ABC123",
        rol=Rol.OPERADOR,
        nuevo_estado=EstadoSolicitud.VALIDADA
    )

    assert solicitud.estado == EstadoSolicitud.VALIDADA
