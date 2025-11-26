from fastapi import APIRouter, UploadFile
from services.ocr_service import OCRService
from services.ai_service import AIService

router = APIRouter()
ocr_service = OCRService()
ai_service = AIService()

@router.post("/documento")
async def validar_documento(file: UploadFile, nombre: str, curp: str):
    # Guardar archivo temporalmente
    path = f"temp/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    # 1. Extraer texto del documento
    texto = ocr_service.extract_text(path)

    # 2. Validar con IA muy básica
    formulario = {
        "nombre": nombre,
        "curp": curp,
    }

    validacion = ai_service.validate_document(texto, formulario)

    return {
        "texto_extraido": texto,
        "validacion": validacion
    }
