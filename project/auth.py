# Author:        F4lnes
# Created        12.03.2021
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)


def check_password(db_pw, password):
    if db_pw[:5] == password[:5]:
        return True


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login_post'))

    login_user(user, remember=remember)
    return redirect(url_for('main.welcome'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(
        email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup_post'))
    new_user = User(email=email, name=name, password=password)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login_post'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

