from flask import Flask, send_file, render_template
from google.cloud import translate

app = Flask(__name__)

@app.route('/')
def usage():
    return'''
        <p> http://HOSTNAME:5001/hello?lang=LANG_CODE </p>
        <pre>
        Language Code
        -------- ----
        Afrikaans 	af
        Albanian 	sq
        Arabic 	ar
        Belarusian 	be
        Bulgarian 	bg
        Catalan 	ca
        Chinese Simplified 	zh-CN
        Chinese Traditional 	zh-TW
        Croatian 	hr
        Czech 	cs
        Danish 	da
        Dutch 	nl
        English 	en
        Estonian 	et
        Filipino 	tl
        Finnish 	fi
        French 	fr
        Galician 	gl
        German 	de
        Greek 	el
        Hebrew 	iw
        Hindi 	hi
        Hungarian 	hu
        Icelandic 	is
        Indonesian 	id
        Irish 	ga
        Italian 	it
        Japanese 	ja
        Korean 	ko
        Latvian 	lv
        Lithuanian 	lt
        Macedonian 	mk
        Malay 	ms
        Maltese 	mt
        Norwegian 	no
        Persian 	fa
        Polish 	pl
        Portuguese 	pt
        Romanian 	ro
        Russian 	ru
        Serbian 	sr
        Slovak 	sk
        Slovenian 	sl
        Spanish 	es
        Swahili 	sw
        Swedish 	sv
        Thai 	th
        Turkish 	tr
        Ukrainian 	uk
        Vietnamese 	vi
        Welsh 	cy
        Yiddish 	yi
        </pre>
        '''

@app.route("/english")
def hello():
  return ""

@app.route("/spanish")
def spanish():
    return "Hola Mundo"

@app.route("/german")
def german():
    return "Hallo Welt"

#@app.route("/hello/<name>")
#def say_hello(name):
#    return "Hello %s" % name

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

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

    return result['translatedText']

@app.route("/image/<filename>")
def get_image(filename):
    return send_file(filename, mimetype='image/jpg')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
