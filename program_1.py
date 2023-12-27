from PIL import Image
from pytesseract import pytesseract
import enum


class OS(enum.Enum):
    Mac = 0
    Window = 1


class Language(enum.Enum):
    ENG = "en"
    AR = "ar"


class ImageReader:
    def __init__(self, os: OS):
        if os == OS.Mac:
            print("Running on: MAC\n")
        if os == OS.Window:
            windows_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = windows_path
            print("Running on: Window \n")

    def extract_text(self, image: str, lang: str) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text

if __name__ == '__main__':
    ir = ImageReader(OS.Mac)
    text = ir.extract_text('question.png', lang='en' )
    print("Document Text: ", text)
