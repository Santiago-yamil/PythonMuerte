from fastapi import FastAPI
from routes.aspirante_router import router as aspirante_router
from routes.validacion_router import router as validacion_router

app = FastAPI(title="Plataforma Integral de Gestión de Apoyos")

# Registrar rutas
app.include_router(aspirante_router, prefix="/aspirante", tags=["Aspirante"])
app.include_router(validacion_router, prefix="/validacion", tags=["Validación"])

@app.get("/")
def root():
    return {"message": "Backend funcionando correctamente."}
