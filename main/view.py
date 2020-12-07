from flask import Blueprint
from article.view import article_api
from login.view import login_api
from search.view import search_api
from replys.view import reply_api
from cafeteria.view import cafeteria_api
from contest.view import contest_api
from admin.view import admin_api
from univ.view import univ_api
from mypage.view import mypage_api

main_api = Blueprint('main', __name__, url_prefix='/')

@main_api.route("/index", methods=['GET'])
def main():
    return 'hello'

api_urls = [article_api, login_api, search_api, main_api, reply_api, cafeteria_api, contest_api, univ_api, mypage_api, admin_api]
