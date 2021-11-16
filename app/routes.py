from werkzeug.urls import url_parse

from app import app
from flask import render_template, Response, flash, redirect, url_for, request
from flask_login import login_user, login_required, current_user

from app.forms import LoginForm
from app.models import User

from camera import WebCam
from camera import PiCamera

#camera = PiCamera(flip=False) # flip pi camera if upside down.
camera = WebCam()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not(user is not None and user.check_password(form.password.data)):
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login'))
        else:
            login_user(user, form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = '/'
            return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/')
@login_required
def index():
    return render_template('index.html') #you can customze index.html here


def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
@login_required
def video_feed():
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')