# app/api/v1/workflow.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.workflow_service import actualizar_estado_solicitud, obtener_transiciones_para_rol, WorkflowError
from app.core.workflow import Rol
from app.models.solicitud import EstadoSolicitud


router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.put("/solicitud/{curp}/estado")
def cambiar_estado(curp: str, rol: Rol, nuevo_estado: EstadoSolicitud, db: Session = Depends(get_db)):

    try:
        solicitud = actualizar_estado_solicitud(db, curp, rol, nuevo_estado)
        return {
            "message": "Estado actualizado correctamente",
            "curp": curp,
            "nuevo_estado": solicitud.estado
        }
    except WorkflowError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/solicitud/{curp}/transiciones")
def transiciones_posibles(curp: str, rol: Rol, db: Session = Depends(get_db)):

    from app.models.solicitud import Solicitud

    solicitud = db.query(Solicitud).filter(Solicitud.curp == curp).first()
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")

    estados = obtener_transiciones_para_rol(rol, solicitud.estado)

    return {
        "estado_actual": solicitud.estado,
        "transiciones_posibles": estados
    }
