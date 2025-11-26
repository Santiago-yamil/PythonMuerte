from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session

from app.schemas.workflow import CambioEstadoRequest
from app.services.workflow_service import actualizar_estado_solicitud, WorkflowError
from app.core.workflow import Rol, EstadoSolicitud
from app.core.config import get_db  # asumiendo que tienes esto para DB
from app.core.security import verificar_token
router = APIRouter(
    prefix="/workflow",
    tags=["workflow"]
)

@router.put("/estado")
def cambiar_estado(request: CambioEstadoRequest, db: Session = Depends(get_db)):
    """
    Cambia el estado de una solicitud según el rol y el workflow.
    """
    try:
        solicitud_actualizada = actualizar_estado_solicitud(
            db=db,
            curp=request.curp,
            rol=request.rol,
            nuevo_estado=request.nuevo_estado
        )
        return {
            "mensaje": f"Solicitud actualizada a {solicitud_actualizada.estado}",
            "curp": solicitud_actualizada.curp,
            "estado": solicitud_actualizada.estado
        }
    except WorkflowError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
def obtener_usuario_actual(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")
    token = authorization.split(" ")[1]
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    # Retornamos info del usuario y su rol
    return {"username": payload.get("sub"), "rol": Rol(payload.get("rol"))}

@router.put("/estado")
def cambiar_estado(
    request: CambioEstadoRequest,
    db: Session = Depends(get_db),
    usuario: dict = Depends(obtener_usuario_actual)
):
    """
    Cambia el estado de una solicitud según el rol y el workflow.
    """
    rol_usuario = usuario["rol"]

    try:
        solicitud_actualizada = actualizar_estado_solicitud(
            db=db,
            curp=request.curp,
            rol=rol_usuario,
            nuevo_estado=request.nuevo_estado
        )
        return {
            "mensaje": f"Solicitud actualizada a {solicitud_actualizada.estado}",
            "curp": solicitud_actualizada.curp,
            "estado": solicitud_actualizada.estado
        }
    except WorkflowError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
