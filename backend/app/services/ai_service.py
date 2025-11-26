class AIService:
    def validate_document(self, ocr_text: str, formulario: dict):
        """Valida si el OCR coincide con los datos esperados."""
        resultados = {}

        for key, valor in formulario.items():
            resultados[key] = valor.lower() in ocr_text.lower()

        return resultados
