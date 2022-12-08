import PyPDF2

pdf = PyPDF2.PdfFileReader(open('resume.pdf', "rb"))
sentences = list()
for page in pdf.pages:
    text = page.extractText()
    sentence = ''
    for i in text:
        if i != '.' and i != '؛' and i != ';':
            sentence += i
        else:
            sentences.append(sentence)
            sentence = ''

for i in sentences:
    print(i, '\n')


