from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from app.schemas.workflow import CambioEstadoRequest
from app.services.workflow_service import actualizar_estado_solicitud, WorkflowError
from app.core.config import get_db
from app.core.security import verificar_token

router = APIRouter(prefix="/workflow", tags=["Workflow"])

# Función para obtener usuario del token
def obtener_usuario_actual(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")
    token = authorization.split(" ")[1]
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return {"username": payload.get("sub"), "rol": payload.get("rol")}

# PUT para cambiar estado
@router.put("/estado")
def cambiar_estado(
    request: CambioEstadoRequest,
    db: Session = Depends(get_db),
    usuario: dict = Depends(obtener_usuario_actual)
):
    try:
        solicitud_actualizada = actualizar_estado_solicitud(
            db=db,
            curp=request.curp,
            rol=usuario["rol"],
            nuevo_estado=request.nuevo_estado
        )
        return {
            "mensaje": f"Solicitud actualizada a {solicitud_actualizada.estado}",
            "curp": solicitud_actualizada.curp,
            "estado": solicitud_actualizada.estado
        }
    except WorkflowError as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET /workflow/ → lista solicitudes
@router.get("/")
def listar_solicitudes(db: Session = Depends(get_db)):
    # Aquí deberías llamar a tu servicio que lista todas las solicitudes
    return {"mensaje": "Lista de solicitudes (pendiente de implementación)"}

# POST /workflow/ → crea solicitud
@router.post("/")
def crear_solicitud():
    return {"mensaje": "Crear solicitud (pendiente)"}

# GET /workflow/{curp} → obtener solicitud
@router.get("/{curp}")
def obtener_solicitud(curp: str):
    return {"mensaje": f"Obtener solicitud {curp} (pendiente)"}

# DELETE /workflow/{curp} → eliminar solicitud
@router.delete("/{curp}")
def eliminar_solicitud(curp: str):
    return {"mensaje": f"Eliminar solicitud {curp} (pendiente)"}
