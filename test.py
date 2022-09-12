from ext import ImgExt

image_text = ImgExt(image_path="img/diabetes.png", file_name="my_new_package2")
  

pk=image_text.get_text()

p = image_text.convert_to_word()
print(p)