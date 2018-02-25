from flask import Flask, render_template
from google.cloud import translate

app = Flask(__name__)

@app.route('/')
def usage():
    client = translate.Client()
    languages = client.get_languages()
    return render_template('usage.html', languages=languages)

@app.route("/hello/<language>")
def translate_hello_world(language):
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()
    text = "Hello World"

    result = translate_client.translate(
        text, target_language=language
    )

    return result['translatedText']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
