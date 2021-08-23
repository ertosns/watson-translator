from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['GET', 'POST'])
def englishToFrench():
    # Write your code here
    english_sentence = request.args.get('textToTranslate')
    return translator.EnglishToFrench(english_sentence)

@app.route("/frenchToEnglish", methods=['GET', 'POST'])
def frenchToEnglish():
    # Write your code here
    french_sentence = request.args.get('textToTranslate')
    return translator.FrenchToEnglish(french_sentence)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    with  open('./templates/index.html') as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
