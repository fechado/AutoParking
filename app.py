
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import current_user, login_user, login_required, LoginManager, logout_user
from flask_session import Session
from config_lang import ConfigLang
from datetime import date, time, datetime

login_manager = LoginManager()

app = Flask(__name__)


#'postgresql://username:password@host:port/database'

uri = 'postgresql://zgnojbpnkhoqmx:5d8d7241e51758b68ce3aa6c365d746d4ea3b8a711a2b5d31c33100ef7a6705a@ec2-44-196-146-152.compute-1.amazonaws.com:5432/d26fib3rqoq9p1' # produccion

#from config import config
#uri = config() # megavas

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(32)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager.init_app(app)
login_manager.login_view = "index"

server_session = Session(app)


langIni = 'lang_ESP.ini'

@app.route("/", methods=["GET", "POST"])
def index():
    if(request.method == "POST"):
        usuario = request.form["user"]
        password = request.form["pass"]
        
        validate = Usuario.login(usuario, password)
        if validate[0]:
            login_user(validate[1])
            return redirect(url_for("ventas"))
    
    lang = ConfigLang(langIni, 'LOGIN')
    return render_template('index.html', lang=lang)

if __name__ == '__main__':
    app.run(debug=False)
