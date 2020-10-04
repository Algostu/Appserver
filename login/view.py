import json, time, requests, re

import pandas as pd
from usernames import is_safe_username
from flask import jsonify, escape, Blueprint, request, session, current_app as app
from sqlalchemy import text
from Crypto.PublicKey import RSA
from Crypto import Random

from main.extensions import flask_bcrypt
from main.model import *

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
    uid = request.args.get('id')
    user_access_token = request.args.get('token')
    # check sender access token is valid
    token_info = get_request(user_access_token, '/v1/user/access_token_info')
    if not token_info or int(uid) != int(token_info['id']):
        return '<Fail>:1:token expired'
    result = UserInfo.query.filter_by(userID = int(uid)).first()
    if not result:
        return json.dumps({'status' : 'fail'})
    # Todo: 다른 추가 정보 저장하기
    # 복호화 하는 방법
    # bcrypt.check_password_hash(pw_hash, 'hunter2').decode('utf-8')
    # user_session['user_hash'] = flask_bcrypt.generate_password_hash(uid)
    # session['token'] = user_session['user_hash']
    result = result.serialize()
    result['status'] = 'success'
    return json.dumps(result)

@login_api.route('/kakaoSignup', methods=['POST'])
def post_signup():
    pattern = re.compile("^(?!_$)(?![-.])(?!.*[_.-]{2})[가-힣a-zA-Z0-9_.-]+(?<![.-])$")
    user_info = request.json
    user_access_token = escape(user_info['accessToken'])
    user_id = escape(user_info['userID'])
    email, gender, ageRange = escape(user_info['email']), escape(user_info['gender']), escape(user_info['ageRange'])
    nickName, grade = escape(user_info['nickName']), escape(user_info['grade'])

    # check sender access token is valid
    token_info = get_request(user_access_token, '/v1/user/access_token_info')
    if not token_info or str(user_id) != str(token_info['id']):
        return '<Fail>:1:token expired'
    # check sender info is valid
    auth_user_info = get_request(user_access_token, '/v2/user/me')
    if not auth_user_info or auth_user_info['kakao_account']['email'] != email or \
    auth_user_info['kakao_account']['gender'] != gender or \
    auth_user_info['kakao_account']['age_range'] != ageRange:
        return '<Fail>:2:sender info is not valid'
    # check if nickName and grade is valid
    ## Todo : nickName validation test
    if not pattern.search(nickName).group() or int(grade) < 9 or int(grade) > 13:
        return '<Fail>:3:nickname or grade is not valid'
    # check if user is possible to enroll school
    schoolInfo = SchoolInfo.query.filter_by(schoolID = user_info['schoolID']).first()
    if not schoolInfo:
        return "<Fail>:7:school id is not good"
    sch_gen = schoolInfo.gender
    sch_reg = schoolInfo.regionID
    if (sch_gen == 1 and gender != 'male') or (sch_gen == 2 and gender != 'female'):
        return "<Fail>:4:user gender is not same as school"
    if str(ageRange) not in ['20~29', '14~19'] or str(ageRange) == '20~29' and int(grade) < 13:
        return "<Fail>:5:user age don't go school any more"
    # check if user has already registered
    if UserInfo.query.filter_by(userID = user_id).first():
        return "<Fail>:6:alread registered"
    # store to user info to db
    gender = 1 if str(gender) == 'male' else 2
    age = 1 if str(ageRange) == "14~19" else 2
    user = UserInfo(userID=int(user_id), schoolID=user_info['schoolID'], regionID=sch_reg,
    email=str(email), grade=int(grade), age=age, gender=gender, nickName=str(nickName))
    db.session.add(user)
    db.session.commit()

    return '<success>'

def get_request(token, url):
    headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    BASE_URL = 'https://kapi.kakao.com'
    URL = BASE_URL + url
    res = requests.get(URL, headers=headers)
    res_json = res.json()
    return res_json
