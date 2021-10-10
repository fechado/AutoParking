from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask.helpers import url_for
from config_lang import ConfigLang


app = Flask(__name__)


langIni = 'lang_ESP.ini'

@app.route("/")
def index():
    lang = ConfigLang(langIni, 'LOGIN')
    return render_template('index.html', lang=lang)

if __name__ == '__main__':
    app.run(debug=False)
