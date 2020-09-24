import json, time
from flask import Blueprint, request, current_app as app
from sqlalchemy import text

article_api = Blueprint('article', __name__, url_prefix='/article')


@article_api.route('/read', methods=['GET'])
def get_read_article():
    articleID = request.args.get('articleID')
    articleType = request.args.get('articleType')
    row = app.db.execute(
    """
    select articleID, isAnonymous, content, title, viewNumber, reply, heart, writtenTime, nickName
    from article JOIN user_info ON article.userID = user_info.userID
    where articleID = %s and communityID = %s
    """, (articleID, articleType)).fetchone()
    article = {}
    if row:
        article = {'articleID': row[0], 'isAnonymous': row[1], 'content':row[2], 'title':row[3],
        'viewNumber':row[4], 'reply':row[5], 'heart':row[6], 'writtenTime':row[7], 'nickName':row[8]}
    return json.dumps(article)


@article_api.route('/write', methods=['POST'])
def post_write_article():
    article = json.loads(request.json)
    if article is None:
        return 'fail'
    now = time.localtime()
    article['time'] = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    result = app.db.execute(text(
    """
    INSERT INTO article (communityID, userID, isAnonymous, title, content)
    VALUES (:articleType, :userId, :isAnonymous, :title, :content)
    """), article)
    return 'success:' + str(result.lastrowid)


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
    articles = [{'articleId': row[0], 'isAnonymous': row[1], 'content':row[2][:25], 'title':row[3][:20],
    'viewNumber':row[4], 'reply':row[5], 'heart':row[6], 'writtenTime':row[7], 'nickName':row[8]} for row in rows]
    return json.dumps(articles)


@article_api.route('/hotArticleList', methods=['GET'])
def get_hot_article_list():
    sql = """
    SELECT articleID, communityID, title, content, heart, reply
    FROM article WHERE heart =
    (SELECT max(heart) FROM article where communityID = %s)
    """
    hot_articles = {}
    for id, name in app.db.execute("select * from community").fetchall():
        hot_article = app.db.execute(sql, id).fetchone()
        if hot_article:
            hot_articles[name] = {"articleID" : hot_article["articleID"], "communityID" : hot_article["communityID"],
            "title" : hot_article["title"][:20], "content" : hot_article["content"][:50],
            "heart" : hot_article["heart"], "reply" : hot_article["reply"]}
    return json.dumps(hot_articles, ensure_ascii=False, indent=4)


@article_api.route('/latestArticleList', methods=['GET'])
def get_latest_article_list():
    sql = """
    SELECT articleID, communityID, title, content, heart, reply
    FROM article where communityID = %s order by writtenTime desc limit 1
    """
    latest_articles = {}
    for id, name in app.db.execute("select * from community").fetchall():
        latest_article = app.db.execute(sql, id).fetchone()
        if latest_article:
            latest_articles[name] = {"articleID" : latest_article["articleID"], "communityID" : latest_article["communityID"],
            "title" : latest_article["title"][:20], "content" : latest_article["content"][:50],
            "heart" : latest_article["heart"], "reply" : latest_article["reply"]}
    return json.dumps(latest_articles, ensure_ascii=False, indent=4)
