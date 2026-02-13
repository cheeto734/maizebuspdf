# import fitz
# source venv/bin/activate to run in venv
# switch environment to venv at bottom right
# deactivate to exit venv
# pip install pymupdf pyinstaller
# 
import fitz


print("hello world")


doc = fitz.open("Map.pdf")

for page in doc:
    text = page.TextPage.extractTEXT()
    print(text)
doc.close()