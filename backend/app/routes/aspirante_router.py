from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Modelo de ejemplo
class Aspirante(BaseModel):
    id: int
    nombre: str
    curp: str

# "Base de datos" en memoria temporal
aspirantes_db: List[Aspirante] = []

# GET todos los aspirantes
@router.get("/")
async def get_aspirantes():
    return aspirantes_db

# GET por ID
@router.get("/{aspirante_id}")
async def get_aspirante(aspirante_id: int):
    for a in aspirantes_db:
        if a.id == aspirante_id:
            return a
    raise HTTPException(status_code=404, detail="Aspirante no encontrado")

# POST nuevo aspirante
@router.post("/")
async def create_aspirante(aspirante: Aspirante):
    aspirantes_db.append(aspirante)
    return aspirante

# PUT actualizar aspirante
@router.put("/{aspirante_id}")
async def update_aspirante(aspirante_id: int, data: Aspirante):
    for i, a in enumerate(aspirantes_db):
        if a.id == aspirante_id:
            aspirantes_db[i] = data
            return data
    raise HTTPException(status_code=404, detail="Aspirante no encontrado")

# DELETE aspirante
@router.delete("/{aspirante_id}")
async def delete_aspirante(aspirante_id: int):
    for i, a in enumerate(aspirantes_db):
        if a.id == aspirante_id:
            aspirantes_db.pop(i)
            return {"message": "Aspirante eliminado"}
    raise HTTPException(status_code=404, detail="Aspirante no encontrado")
