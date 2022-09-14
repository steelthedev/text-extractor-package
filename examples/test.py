from image_extract.ext import ImgExt

img = ImgExt(image_path="image_path",file_name="test")

# To return text

text=img.get_text()

print(text)

# To convert text to docx
img.convert_to_word()