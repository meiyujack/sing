from flask import url_for, flash, send_from_directory
from flask_login import login_user
from sing.forms import LoginForm
from sing.models import db, User, Singer, Album, Track
from sing.utils import turn_row_into_tuple

from flask import request, render_template, redirect, Blueprint,current_app
from sqlalchemy import select

import datetime
import random
import json

user_bp = Blueprint("user", __name__)


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        login_form = LoginForm()
        return render_template('login.html', form=login_form)
    if request.method == "POST":
        nickname = request.form.get("nickname")
        password = request.form.get("password")

        curr_user = db.session.execute(
            select(User).where(User.nickname == nickname)).first()
        if curr_user:
            curr_user = curr_user[0]
            if curr_user.check_password(password):
                login_user(curr_user,
                           remember=request.form.get("remember"),
                           duration=datetime.timedelta(days=3))
                return redirect(url_for("user.select_all"))
            else:
                flash("用户名或密码错误", category="info")
                return ""
        else:
            flash("用户名或密码错误", category="info")
            return ""


@user_bp.route("/whole")
def select_all():
    singers = db.session.execute(select(Singer.id, Singer.name)).all()
    albums = db.session.execute(select(Album.id, Album.name)).all()
    tracks = db.session.execute(select(Track.id, Track.name)).all()
    print(singers, albums, tracks)
    return render_template("whole.html",
                           singers=turn_row_into_tuple(singers),
                           albums=turn_row_into_tuple(albums),
                           tracks=turn_row_into_tuple(tracks))



@user_bp.route("/")
def base():
    print(current_app.static_folder)
    print(current_app.static_url_path)
    # return send_from_directory('front','index.html')
    return send_from_directory('static/front','index.html')


@user_bp.route("/<path:path>")
def home(path):
    return send_from_directory('static/front/public', path)


@user_bp.route("/rand")
def hello():
    return str(random.randint(0, 100))

@user_bp.route("/randData")
def randData():
    print('randData')
    params = request.args.get('params')
    randomNumber = random.randint(0, 100)

    data = json.dumps({
        "randomNumber": str(randomNumber), 
        "params": str(int(params)), 
        "sumRandomParams": str(randomNumber + int(params))
        })
    
    print(data)
    return data

