# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from sqlalchemy.schema import FetchedValue
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin


db = SQLAlchemy()

# Define models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('web_user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class WebUser(db.Model, UserMixin):
    __tablename__ = 'web_user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('web_users', lazy='dynamic'))

    def __str__(self):
        return self.email

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class SignOutUser(db.Model):
    __tablename__ = 'signout_user'

    userID = db.Column(db.Integer, primary_key=True)
    writtenTime = db.Column(db.DateTime)

class CommunityAll(db.Model):
    __tablename__ = 'community_all'

    communityID = db.Column(db.Integer, primary_key=True)
    communityName = db.Column(db.String(20, 'utf8_unicode_ci'))

class LikeToAll(db.Model):
    __tablename__ = 'like_to_all'

    likeID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    articleID = db.Column(db.ForeignKey('article_all.articleID', ondelete='CASCADE'), index=True)

    user_info = db.relationship('UserInfo', primaryjoin='LikeToAll.userID == UserInfo.userID', backref='like_to_alls')
    article = db.relationship('ArticleAll', primaryjoin='LikeToAll.articleID == ArticleAll.articleID', backref='like_to_alls')

class LikeToSchool(db.Model):
    __tablename__ = 'like_to_school'

    likeID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    articleID = db.Column(db.ForeignKey('article_school.articleID', ondelete='CASCADE'), index=True)

    user_info = db.relationship('UserInfo', primaryjoin='LikeToSchool.userID == UserInfo.userID', backref='like_to_schools')
    article = db.relationship('ArticleSchool', primaryjoin='LikeToSchool.articleID == ArticleSchool.articleID', backref='like_to_schools')

class LikeToRegion(db.Model):
    __tablename__ = 'like_to_region'

    likeID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    articleID = db.Column(db.ForeignKey('article_region.articleID', ondelete='CASCADE'), index=True)

    user_info = db.relationship('UserInfo', primaryjoin='LikeToRegion.userID == UserInfo.userID', backref='like_to_regions')
    article = db.relationship('ArticleRegion', primaryjoin='LikeToRegion.articleID == ArticleRegion.articleID', backref='like_to_regions')


class CommunityRegion(db.Model):
    __tablename__ = 'community_region'

    communityID = db.Column(db.Integer, primary_key=True)
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    communityName = db.Column(db.String(20, 'utf8_unicode_ci'))

    region_info = db.relationship('RegionInfo', primaryjoin='CommunityRegion.regionID == RegionInfo.regionID', backref='community_regions')

class CommunitySchool(db.Model):
    __tablename__ = 'community_school'

    communityID = db.Column(db.Integer, primary_key=True)
    schoolID = db.Column(db.ForeignKey('school_info.schoolID', ondelete='CASCADE'), nullable=False, index=True)
    communityName = db.Column(db.String(20, 'utf8_unicode_ci'))

    school_info = db.relationship('SchoolInfo', primaryjoin='CommunitySchool.schoolID == SchoolInfo.schoolID', backref='community_schools')

class ArticleAll(db.Model):
    __tablename__ = 'article_all'

    articleID = db.Column(db.Integer, primary_key=True)
    communityID = db.Column(db.ForeignKey('community_all.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)
    title = db.Column(db.String(50, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    viewNumber = db.Column(db.Integer, server_default=FetchedValue())
    reply = db.Column(db.Integer, server_default=FetchedValue())
    heart = db.Column(db.Integer, server_default=FetchedValue())
    writtenTime = db.Column(db.DateTime)

    community = db.relationship('CommunityAll', primaryjoin='ArticleAll.communityID == CommunityAll.communityID', backref='article_alls')
    user_info = db.relationship('UserInfo', primaryjoin='ArticleAll.userID == UserInfo.userID', backref='article_alls')

class ArticleRegion(db.Model):
    __tablename__ = 'article_region'

    articleID = db.Column(db.Integer, primary_key=True)
    communityID = db.Column(db.ForeignKey('community_region.communityID', ondelete='CASCADE'), index=True)
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)
    title = db.Column(db.String(50, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    viewNumber = db.Column(db.Integer, server_default=FetchedValue())
    reply = db.Column(db.Integer, server_default=FetchedValue())
    heart = db.Column(db.Integer, server_default=FetchedValue())
    writtenTime = db.Column(db.DateTime)

    community = db.relationship('CommunityRegion', primaryjoin='ArticleRegion.communityID == CommunityRegion.communityID', backref='article_regions')
    user_info = db.relationship('UserInfo', primaryjoin='ArticleRegion.userID == UserInfo.userID', backref='article_regions')
    region_info = db.relationship('RegionInfo', primaryjoin='ArticleRegion.regionID == RegionInfo.regionID', backref='article_regions')


class ArticleSchool(db.Model):
    __tablename__ = 'article_school'

    articleID = db.Column(db.Integer, primary_key=True)
    communityID = db.Column(db.ForeignKey('community_school.communityID', ondelete='CASCADE'), index=True)
    schoolID = db.Column(db.ForeignKey('school_info.schoolID', ondelete='CASCADE'), nullable=False, index=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)
    title = db.Column(db.String(50, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    viewNumber = db.Column(db.Integer, server_default=FetchedValue())
    reply = db.Column(db.Integer, server_default=FetchedValue())
    heart = db.Column(db.Integer, server_default=FetchedValue())
    writtenTime = db.Column(db.DateTime)

    community = db.relationship('CommunitySchool', primaryjoin='ArticleSchool.communityID == CommunitySchool.communityID', backref='articles')
    user_info = db.relationship('UserInfo', primaryjoin='ArticleSchool.userID == UserInfo.userID', backref='article_schools')
    school_info = db.relationship('SchoolInfo', primaryjoin='ArticleSchool.schoolID == SchoolInfo.schoolID', backref='user_info_schools')

class RegionInfo(db.Model):
    __tablename__ = 'region_info'

    regionID = db.Column(db.Integer, primary_key=True)
    regionName = db.Column(db.String(20, 'utf8_unicode_ci'))


class SchoolInfo(db.Model):
    __tablename__ = 'school_info'

    schoolID = db.Column(db.Integer, primary_key=True)
    studentNum = db.Column(db.Integer)
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    regionName = db.Column(db.String(100, 'utf8_unicode_ci'))
    townName = db.Column(db.String(100, 'utf8_unicode_ci'))
    schoolName = db.Column(db.String(1000, 'utf8_unicode_ci'))
    gender = db.Column(db.Integer)
    contact = db.Column(db.String(20, 'utf8_unicode_ci'))
    homePage = db.Column(db.String(1000, 'utf8_unicode_ci'))

    region_info = db.relationship('RegionInfo', primaryjoin='SchoolInfo.regionID == RegionInfo.regionID', backref='school_infos')


class UnivInfo(db.Model):
    __tablename__ = 'univ_info'

    univID = db.Column(db.Integer, primary_key=True)
    univName = db.Column(db.String(100, 'utf8_unicode_ci'))
    subRegion = db.Column(db.String(100, 'utf8_unicode_ci'))
    homePage = db.Column(db.String(1000, 'utf8_unicode_ci'))
    eduHomePage = db.Column(db.String(300, 'utf8_unicode_ci'))
    logoPossible = db.Column(db.Integer)

class CafeteriaInfo(db.Model):
    __tablename__ = 'cafeteria_info'

    schoolID = db.Column(db.Integer, primary_key=True)
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    version = db.Column(db.DateTime)
    cafeMenu = db.Column(db.String(7000, 'utf8_unicode_ci'))

class ContestInfo(db.Model):
    __tablename__ = 'contest_info'

    contestID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100, 'utf8_unicode_ci'))
    imageUrl = db.Column(db.String(100, 'utf8_unicode_ci'))
    content = db.Column(db.String(7000, 'utf8_unicode_ci'))
    area = db.Column(db.String(100, 'utf8_unicode_ci'))
    sponsor = db.Column(db.String(100, 'utf8_unicode_ci'))
    start = db.Column(db.String(100, 'utf8_unicode_ci'))
    end = db.Column(db.String(100, 'utf8_unicode_ci'))
    prize = db.Column(db.String(100, 'utf8_unicode_ci'))
    firstPrize = db.Column(db.String(100, 'utf8_unicode_ci'))
    homePage = db.Column(db.String(100, 'utf8_unicode_ci'))


class UserCredential(db.Model):
    __tablename__ = 'user_credential'

    userID = db.Column(db.Integer, primary_key=True)
    pwd = db.Column(db.String(20, 'utf8_unicode_ci'))



class UserInfo(db.Model):
    __tablename__ = 'user_info'

    userID = db.Column(db.Integer, primary_key=True)
    schoolID = db.Column(db.ForeignKey('school_info.schoolID', ondelete='CASCADE'), nullable=False, index=True)
    schoolName = db.Column(db.String(100, 'utf8_unicode_ci'), nullable=False)
    regionName = db.Column(db.String(100, 'utf8_unicode_ci'), nullable=False)
    studentName = db.Column(db.String(100, 'utf8_unicode_ci'), nullable=False)
    authorized = db.Column(db.Integer)
    signupDate = db.Column(db.DateTime)
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    email = db.Column(db.String(100, 'utf8_unicode_ci'), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)

    school_info = db.relationship('SchoolInfo', primaryjoin='UserInfo.schoolID == SchoolInfo.schoolID', backref='user_infos')
    region_info = db.relationship('RegionInfo', primaryjoin='UserInfo.regionID == RegionInfo.regionID', backref='user_infos')


class ReplyAll(db.Model):
    __tablename__ = 'reply_all'

    replyID = db.Column(db.Integer, primary_key=True)
    articleID = db.Column(db.ForeignKey('article_all.articleID', ondelete='CASCADE'), index=True)
    communityID = db.Column(db.ForeignKey('community_all.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    writtenTime = db.Column(db.DateTime)

    article = db.relationship('ArticleAll', primaryjoin='ReplyAll.articleID == ArticleAll.articleID', backref='reply_alls')
    community = db.relationship('CommunityAll', primaryjoin='ReplyAll.communityID == CommunityAll.communityID', backref='reply_alls')
    user_info = db.relationship('UserInfo', primaryjoin='ReplyAll.userID == UserInfo.userID', backref='reply_alls')

class ReplyRegion(db.Model):
    __tablename__ = 'reply_region'

    replyID = db.Column(db.Integer, primary_key=True)
    articleID = db.Column(db.ForeignKey('article_region.articleID', ondelete='CASCADE'), index=True)
    communityID = db.Column(db.ForeignKey('community_region.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    writtenTime = db.Column(db.DateTime)

    article = db.relationship('ArticleRegion', primaryjoin='ReplyRegion.articleID == ArticleRegion.articleID', backref='reply_regions')
    community = db.relationship('CommunityRegion', primaryjoin='ReplyRegion.communityID == CommunityRegion.communityID', backref='reply_regions')
    user_info = db.relationship('UserInfo', primaryjoin='ReplyRegion.userID == UserInfo.userID', backref='reply_regions')


class ReplySchool(db.Model):
    __tablename__ = 'reply_school'

    replyID = db.Column(db.Integer, primary_key=True)
    articleID = db.Column(db.ForeignKey('article_school.articleID', ondelete='CASCADE'), index=True)
    communityID = db.Column(db.ForeignKey('community_school.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID', ondelete='CASCADE'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    writtenTime = db.Column(db.DateTime)

    article = db.relationship('ArticleSchool', primaryjoin='ReplySchool.articleID == ArticleSchool.articleID', backref='reply_schools')
    community = db.relationship('CommunitySchool', primaryjoin='ReplySchool.communityID == CommunitySchool.communityID', backref='reply_schools')
    user_info = db.relationship('UserInfo', primaryjoin='ReplySchool.userID == UserInfo.userID', backref='reply_schools')


class ReReplySchool(db.Model):
    __tablename__ = 'rereply_school'

    replyID = db.Column(db.Integer, primary_key=True)
    parentReplyID = db.Column(db.ForeignKey('reply_school.replyID', ondelete='CASCADE'), index=True)
    articleID = db.Column(db.ForeignKey('article_school.articleID', ondelete='CASCADE'), index=True)
    communityID = db.Column(db.ForeignKey('community_school.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    writtenTime = db.Column(db.DateTime)

    article = db.relationship('ArticleSchool', primaryjoin='ReReplySchool.articleID == ArticleSchool.articleID', backref='rereplie_schools')
    community = db.relationship('CommunitySchool', primaryjoin='ReReplySchool.communityID == CommunitySchool.communityID', backref='rereplie_schools')
    user_info = db.relationship('UserInfo', primaryjoin='ReReplySchool.userID == UserInfo.userID', backref='rereplie_schools')
    reply = db.relationship('ReplySchool', primaryjoin='ReReplySchool.parentReplyID == ReplySchool.replyID', backref='rereplie_schools')


class ReReplyRegion(db.Model):
    __tablename__ = 'rereply_region'

    replyID = db.Column(db.Integer, primary_key=True)
    parentReplyID = db.Column(db.ForeignKey('reply_region.replyID', ondelete='CASCADE'), index=True)
    articleID = db.Column(db.ForeignKey('article_region.articleID', ondelete='CASCADE'), index=True)
    communityID = db.Column(db.ForeignKey('community_region.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    writtenTime = db.Column(db.DateTime)

    article = db.relationship('ArticleRegion', primaryjoin='ReReplyRegion.articleID == ArticleRegion.articleID', backref='rereplie_regions')
    community = db.relationship('CommunityRegion', primaryjoin='ReReplyRegion.communityID == CommunityRegion.communityID', backref='rereplie_regions')
    user_info = db.relationship('UserInfo', primaryjoin='ReReplyRegion.userID == UserInfo.userID', backref='rereplie_regions')
    reply = db.relationship('ReplyRegion', primaryjoin='ReReplyRegion.parentReplyID == ReplyRegion.replyID', backref='rereplie_regions')

class ReReplyAll(db.Model):
    __tablename__ = 'rereply_all'

    replyID = db.Column(db.Integer, primary_key=True)
    parentReplyID = db.Column(db.ForeignKey('reply_all.replyID', ondelete='CASCADE'), index=True)
    articleID = db.Column(db.ForeignKey('article_all.articleID', ondelete='CASCADE'), index=True)
    communityID = db.Column(db.ForeignKey('community_all.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID'), index=True)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    writtenTime = db.Column(db.DateTime)

    article = db.relationship('ArticleAll', primaryjoin='ReReplyAll.articleID == ArticleAll.articleID', backref='rereplie_alls')
    community = db.relationship('CommunityAll', primaryjoin='ReReplyAll.communityID == CommunityAll.communityID', backref='rereplie_alls')
    user_info = db.relationship('UserInfo', primaryjoin='ReReplyAll.userID == UserInfo.userID', backref='rereplie_alls')
    reply = db.relationship('ReplyAll', primaryjoin='ReReplyAll.parentReplyID == ReplyAll.replyID', backref='rereplie_alls')
