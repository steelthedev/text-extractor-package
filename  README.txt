
# Text-Image-Extractor

This package helps to extract text from clear images such as screenshots, scanned pictures etc.

The following steps demonstrate how to use this package:

### Prerequisites

* Pytesseract must be installed on your local devices.
* For Linux users, you must install pytesseract OCR using sudo

### Install package

To install, use the code below.

```
pip install extract-img-text

```
### Extract text 
To extract the text into your terminal, run the following

```
from image_extract.ext import ImgExt

#uncomment if you are a window user 

#pytesseract.tesseract_cmd = path_to_tesseract_on _your_device 

img = ImgExt(image_path="image_path",file_name="test")

# To return text

text=img.get_text()

print(text)

# To convert text to docx
img.convert_to_word()

```
