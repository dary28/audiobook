import pyttsx3
import PyPDF2
speaker = pyttsx3.init()
path = input('Enter path')
book = open(path,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
for pnum in range(pages):
    page = pdfReader.getPage(pnum)
    text = page.extractText()
    speaker.setProperty("rate",150)
    speaker.say(text)
    speaker.runAndWait()