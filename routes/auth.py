from flask import Blueprint, request, redirect, url_for, render_template
from db.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return redirect(url_for('index'))
    else:
        return render_template('index.html', error="Invalid credentials")