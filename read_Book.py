import pyttsx3
import PyPDF2


speck = pyttsx3.init()
rate = speck.getProperty('rate')
print (rate)
speck.setProperty('rate', 125)

volume = speck.getProperty('volume')
print (volume)
speck.setProperty('volume',1.0)

voices = speck.getProperty('voices')

speck.setProperty('voice', voices[4].id)



url = '/home/karthik/Documents/NS/Module_3__WebSecurity.pdf'

book = open(url,'rb')
pdfReader = PyPDF2.PdfReader(book)

# for i in range(len(voices)):
#     print(i)
#     speck.setProperty('voice', voices[i].id)
#     speck.say('hi karthik')
#     speck.runAndWait()

pages = pdfReader.numPages
print(pages)


for i in range(1,pages):
    print(i)
    page = pdfReader.getPage(i)
    text = page.extractText()
    speck.say(text)
    speck.runAndWait()



# 3,4,11,12,15,33,36,37,41,43,51,