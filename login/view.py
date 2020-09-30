import json, time
from flask import Blueprint, request, session, current_app as app
from sqlalchemy import text
from Crypto.PublicKey import RSA
from Crypto import Random

from main.extensions import flask_bcrypt

login_api = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_token = session.get('token')
        if session_token is None:
            return "fail"
        return f(*args, **kwargs)
    return decorated_function

@login_api.route('/login', methods=['GET'])
def get_login():
    user_session = {}
    uid = request.args.get('userID')
    result = app.db.execute(
    """
    SELECT FROM user_info where userID = %s
    """, (uid)).fetchone()
    if result:
        # Todo: 다른 추가 정보 저장하기
        # 복호화 하는 방법
        # bcrypt.check_password_hash(pw_hash, 'hunter2').decode('utf-8')
        user_session['user_hash'] = flask_bcrypt.generate_password_hash(uid)
        session['token'] = user_session['user_hash']
        return user_session['user_hash']
    else:
        return 'not allowed'

@login_api.route('/signup', methods=['POST'])
def post_signup():
    result = app.db.execute(text(
    """
    INSERT INTO user_info (userID, schoolID, grade, age, userName, nickName)
    VALUES (:userID, :schoolID, :grade, :age,  "hello", :nickName)
    """), request.json)

    return 'success'
