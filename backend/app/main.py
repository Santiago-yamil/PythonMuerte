from fastapi import FastAPI
from app.routes.aspirante_router import router as aspirante_router
from app.routes.validacion_router import router as validacion_router
from app.routes.workflow_router import router as workflow_router


app = FastAPI(title="Plataforma Integral de Gestión de Apoyos")

# Registrar rutas existentes
app.include_router(aspirante_router, prefix="/aspirante", tags=["Aspirante"])
app.include_router(validacion_router, prefix="/validacion", tags=["Validación"])

# Registrar nueva ruta de workflow
app.include_router(workflow_router)



@app.get("/")
def root():
    return {"message": "Backend funcionando correctamente."}

