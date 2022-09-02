import imp
from PIL import Image
from pytesseract import pytesseract
import os

#define path to tesseract

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'

pytesseract.tesseract_cmd = path_to_tesseract

#define path to image

path_to_images = r'images/'

for root,dirs,file_names in os.walk(path_to_images):

    for file_name in file_names:
        img = Image.open(path_to_images + file_name)
        text = pytesseract.image_to_string(img)
        print(text)

