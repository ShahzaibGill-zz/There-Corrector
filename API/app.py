import nltk as nlp
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
nlp.data.path.append('./nltk_data/')
@app.route('/')
def index():
    return 'Please Enter Text'

@app.route('/<string:text>')
def stringCorrector(text):
    inputText = nlp.word_tokenize(text)
    text_array = nlp.pos_tag(inputText)
    for index, word in enumerate(inputText):
        if word in ('There', 'there', 'Their', 'their', '\'re'):
            if text_array[index + 1][1] in ('VB', 'VBD', 'VBN', 'VBP', 'VBZ', 'MD'):

                if index == 0 or index - 1 >= 0 and inputText[index - 1] == '.':
                    inputText[index] = 'There'
                else:
                    inputText[index] = 'there'
            elif text_array[index + 1][1] in ('NN', 'NNS', 'NNP', 'NNPS'):
                if index == 0 or index - 1 >= 0 and inputText[index - 1] == '.':
                    inputText[index] = 'Their'
                else:
                    inputText[index] = 'their'
            elif text_array[index + 1][1] in ('IN', 'JJ', 'VBG'):
                if inputText[index - 1] in ('they', 'They'):
                    inputText[index - 1] = ''
                if index == 0 or index - 1 >= 0 and inputText[index - 1] == '.':
                    inputText[index] = 'They\'re'
                else:
                    inputText[index] = 'they\'re'
    outputText = ' '.join(inputText)
    return outputText

if __name__ == "__main":
    app.run()