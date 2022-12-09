import pdfplumber

with pdfplumber.open(r'Daddy-Long-Legs.pdf') as pdf:
    sentences = list()
    for page in pdf.pages:
        text = page.extract_text()
        sentence = ''
        for i in text:
            if i != '.' and i != '؛' and i != ';':
                sentence += i
            else:
                sentences.append(sentence)
                sentence = ''

    for i in sentences:
        print(i, '\n \n \n \n')

    print(sentence)

