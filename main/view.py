from flask import Blueprint
from article.view import article_api
from login.view import login_api
from search.view import search_api
from replys.view import reply_api

main_api = Blueprint('main', __name__, url_prefix='/')

@main_api.route("/index", methods=['GET'])
def main():
    return 'hello'

api_urls = [article_api, login_api, search_api, main_api, reply_api]
