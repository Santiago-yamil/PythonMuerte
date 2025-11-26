import pytesseract
from PIL import Image

class OCRService:
    def extract_text(self, file_path: str) -> str:
        try:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image, lang="spa")
            return text
        except Exception as e:
            return f"Error en OCR: {e}"
