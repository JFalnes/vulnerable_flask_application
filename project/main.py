# Author:        F4lnes
# Created        12.03.2021
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from sqlalchemy import text
from . import db
from .models import User
from .auth import check_password

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/cheatsheet')
def cheatsheet():
    return render_template('cheatsheet.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/info')
def info():
    return render_template('info.html')


@main.route('/signup')
def signup():
    return render_template('signup.html')


@main.route('/search')
def search():
    return render_template('search.html')


@main.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')


@main.route('/search', methods=['POST'])
def results():
    item_no = []
    item_name = []
    qty = []
    price = []

    sql = text(f"select * from products where item_name LIKE '%{request.form.get('search')}%'")

    result = db.engine.execute(sql)

    for r in result:
        item_no.append(r['item_no'])
        item_name.append(r['item_name'])
        qty.append(r['qty'])
        price.append(r['price'])

    return render_template('results.html', item_no=item_no, item_name=item_name, qty=qty, price=price, len=len(item_no))


@main.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html', name=current_user.name)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
