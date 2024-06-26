from PIL import Image
import pytesseract

image_path = '/home/alex/PycharmProjects/pythonProject3/uploaded_files/6c071d41-3909-4e3b-96c3-9f4ee9f4d84c.png'

img = Image.open(image_path)

text = pytesseract.image_to_string(img)
print(text)