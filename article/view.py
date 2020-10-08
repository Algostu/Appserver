import json, time
from flask import jsonify, make_response, escape, Blueprint, request, session, current_app as app
from sqlalchemy import text
from main.extensions import *
from main.model import *

article_api = Blueprint('article', __name__, url_prefix='/article')

com_type = [ArticleAll, ArticleRegion, ArticleSchool]

@article_api.route('/read', methods=['GET'])
@login_required
@allowed_access
def get_read_article():
    communityType = int(request.args.get('communityType'))
    articleID = int(request.args.get('articleID'))
    article = com_type[communityType]
    # query db and change to dict
    query_result = article.query.filter_by(articleID=articleID).first()
    if not query_result:
        return json.dumps({'status':'fail'})
    target_article = convert_to_dict(query_result)
    target_article.pop('userID')
    #  increase view number
    query_result.viewNumber += 1
    db.session.commit()
    return json.dumps(target_article)

# For future use
# request.on_json_loading_failed = on_json_loading_failed_return_dict
# def on_json_loading_failed_return_dict(e):
#     return {}

@article_api.route('/write', methods=['POST'])
@login_required
@allowed_access
def post_write_article():
    written_info = request.json
    if written_info is None:
        return 'fail'
    # get time and nickName info
    now = time.localtime()
    written_time = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    nickname = '익명' if written_info['isAnonymous'] else session['nick_name']
    # generate articleID
    article_id = (written_info['communityID'] % 100) * 10000000 + get_random_numeric_value(2) * 100000 + current_milli_time()
    # create article instante
    article = com_type[written_info['communityType']]
    new_article = article(articleID=article_id,
    communityID=written_info['communityID'],
    userID=session['user_id'],
    nickName=nickname,
    title=written_info['title'],
    content=written_info['content'],
    writtenTime=written_time, heart = 0, viewNumber = 0, reply = 0)
    db.session.add(new_article)
    db.session.commit()
    return 'success'


@article_api.route('/delete', methods=['GET'])
def get_delete_article():
    userID = request.args.get('userID')
    articleID = request.args.get('articleID')
    articleType = request.args.get('articleType')

    app.db.execute(
    """
    DELETE from article where userID=%s and articleId=%s and communityID=%s
    """, (userID,articleID,articleType))
    return 'success'


@article_api.route('/articleList', methods=['GET'])
def get_article_list():
    articleType = request.args.get('articleType')
    articleTime = request.args.get('articleTime')
    if articleTime == 'latest':
        sql = """
        select articleID, isAnonymous, content, title, viewNumber, reply, heart, writtenTime, nickName
        from article JOIN user_info ON article.userID = user_info.userID
        where communityID=%s order by articleID desc limit 25
        """
        rows = app.db.execute(sql, (articleType)).fetchall()
    else:
        # 동시에 쓰는건 나중에 생각하자
        sql = """
        select articleID, isAnonymous, content, title, viewNumber, reply, heart, writtenTime, nickName
        from article JOIN user_info ON article.userID = user_info.userID
        where communityID=%s and writtenTime < %s
        order by writtenTime desc limit 25
        """
        rows = app.db.execute(sql, (articleType, articleTime)).fetchall()
    articles = [ ]
    for row in rows:
        if row[1]:
            nickName = 'Anonymous'
        else:
            nickName = row[8]

        articles.append({'articleId': row[0], 'content':row[2][:25], 'title':row[3][:20],
        'viewNumber':row[4], 'reply':row[5], 'heart':row[6], 'writtenTime':str(row[7]), 'nickName':nickName})

    return json.dumps(articles)


@article_api.route('/hotArticleList', methods=['GET'])
def get_hot_article_list():
    sql = """
    SELECT articleID, communityID, title, content, heart, reply
    FROM article WHERE heart =
    (SELECT max(heart) FROM articleAll where communityID = %s)
    """
    hot_articles = []
    for id, name in app.db.execute("select * from community").fetchall():
        hot_article = app.db.execute(sql, id).fetchone()
        if hot_article:
            hot_articles.append({"articleID" : hot_article["articleID"], "communityID" : hot_article["communityID"],
            "title" : hot_article["title"][:20], "content" : hot_article["content"][:50],
            "heart" : hot_article["heart"], "reply" : hot_article["reply"]})
            hot_article = None
    return json.dumps(hot_articles, ensure_ascii=False, indent=4)


@article_api.route('/latestArticleList', methods=['GET'])
@login_required
def get_latest_article_list():
    sql = """
    SELECT articleID, communityID, title, content, heart, reply
    FROM article where communityID = %s order by writtenTime desc limit 1
    """
    latest_articles = []
    for id, name in app.db.execute("select * from community").fetchall():
        latest_article = app.db.execute(sql, id).fetchone()
        if latest_article:
            latest_articles.append(convert_to_dict(latest_article))
    return json.dumps(latest_articles, ensure_ascii=False, indent=4)
