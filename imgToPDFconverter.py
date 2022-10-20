
import img2pdf # pip install img2pdf
from PIL import Image
import os

img_path = "" # Enter the path of the image

pdf_path = "" # Enter the path of the pdf

image = Image.open(img_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()

print("Successfully made pdf file")
