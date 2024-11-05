from flask import Flask, render_template, request
import langid
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

def detect_and_translate(text, target_lang):
    # Detect language
    lang, _ = langid.classify(text)

    # Translate language
    translator = Translator()
    translate_text = translator.translate(text, dest=target_lang).text

    return lang, translate_text

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    translation = ""
    detected_lang = ""
    input_text = ""
    if request.method == 'POST':
        input_text = request.form['text']
        target_lang = request.form['target_lang']
        detected_lang, translation = detect_and_translate(input_text, target_lang)

    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=LANGUAGES, text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
