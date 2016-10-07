import nltk as nlp
import re
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
    # Tags each word with part of speech tags. Refer to Penn Treebank Project for more information
    taggedText = nlp.pos_tag(inputText)
    for index, word in enumerate(inputText):
        if word in ('There', 'there', 'Their', 'their') or (word == '\'re' and inputText[index - 1] in ('they', 'They')):
            # Since "They're" is split between two indexes, delete previous index so corrected word is not appended to "They"
            if word == '\'re' and inputText[index - 1] in ('they', 'They'):
                del inputText[index - 1]
                del taggedText[index -1]
                index = index - 1
            if taggedText[index + 1][1] in ('VB', 'VBD', 'VBN', 'VBP', 'VBZ', 'MD','DT'):
                if index == 0 or (index - 1 >= 0 and inputText[index - 1] == '.'):
                    inputText[index] = 'There'
                else:
                    inputText[index] = 'there'
            elif taggedText[index + 1][1] in ('NN', 'NNS', 'NNP', 'NNPS', 'JJS'):
                if index == 0 or (index - 1 >= 0 and inputText[index - 1] == '.'):
                    inputText[index] = 'Their'
                else:
                    inputText[index] = 'their'
            elif taggedText[index + 1][1] in ('IN', 'JJ', 'JJR' 'VBG', 'RB','RBR','RBS','PDT','UH'):
                if index == 0 or (index - 1 >= 0 and inputText[index - 1] == '.'):
                    inputText[index] = 'They\'re'
                else:
                    inputText[index] = 'they\'re'
    outputText = re.sub(r' (\W)',r'\1',' '.join(inputText))
    return outputText

if __name__ == "__main":
    app.run()