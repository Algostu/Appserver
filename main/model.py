# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from sqlalchemy.schema import FetchedValue


db = SQLAlchemy()

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class CommunityAll(db.Model):
    __tablename__ = 'community_all'

    communityID = db.Column(db.Integer, primary_key=True)
    communityName = db.Column(db.String(20, 'utf8_unicode_ci'))

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
    userID = db.Column(db.ForeignKey('user_info.userID'), index=True)
    isAnonymous = db.Column(db.Integer)
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
    userID = db.Column(db.ForeignKey('user_info.userID'), index=True)
    isAnonymous = db.Column(db.Integer)
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
    userID = db.Column(db.ForeignKey('user_info.userID'), index=True)
    isAnonymous = db.Column(db.Integer)
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
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    regionName = db.Column(db.String(100, 'utf8_unicode_ci'))
    townName = db.Column(db.String(100, 'utf8_unicode_ci'))
    schoolName = db.Column(db.String(1000, 'utf8_unicode_ci'))
    gender = db.Column(db.Integer)
    contact = db.Column(db.String(20, 'utf8_unicode_ci'))
    homePage = db.Column(db.String(1000, 'utf8_unicode_ci'))

    region_info = db.relationship('RegionInfo', primaryjoin='SchoolInfo.regionID == RegionInfo.regionID', backref='school_infos')


class CafeteriaInfo(db.Model):
    __tablename__ = 'cafeteria_info'

    schoolID = db.Column(db.Integer, primary_key=True)
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    cafeMenu = db.Column(db.String(7000, 'utf8_unicode_ci'))


class UserCredential(db.Model):
    __tablename__ = 'user_credential'

    userID = db.Column(db.Integer, primary_key=True)
    pwd = db.Column(db.String(20, 'utf8_unicode_ci'))



class UserInfo(db.Model, Serializer):
    __tablename__ = 'user_info'

    userID = db.Column(db.Integer, primary_key=True)
    schoolID = db.Column(db.ForeignKey('school_info.schoolID', ondelete='CASCADE'), nullable=False, index=True)
    regionID = db.Column(db.ForeignKey('region_info.regionID', ondelete='CASCADE'), index=True)
    email = db.Column(db.String(100, 'utf8_unicode_ci'), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    nickName = db.Column(db.String(20, 'utf8_unicode_ci'), nullable=False)

    school_info = db.relationship('SchoolInfo', primaryjoin='UserInfo.schoolID == SchoolInfo.schoolID', backref='user_infos')
    region_info = db.relationship('RegionInfo', primaryjoin='UserInfo.regionID == RegionInfo.regionID', backref='user_infos')

    def serialize(self):
        d = Serializer.serialize(self)
        del d['school_info']
        del d['region_info']
        return d


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

    def serialize(self):
        d = Serializer.serialize(self)
        del d['article']
        del d['community']
        del d['user_info']
        d['writtenTime'] = str(d['writtenTime'])
        return d

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

    def serialize(self):
        d = Serializer.serialize(self)
        del d['article']
        del d['community']
        del d['user_info']
        d['writtenTime'] = str(d['writtenTime'])
        return d

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

    def serialize(self):
        d = Serializer.serialize(self)
        del d['article']
        del d['community']
        del d['user_info']
        d['writtenTime'] = str(d['writtenTime'])
        return d

class ReReplySchool(db.Model):
    __tablename__ = 'rereply_school'

    reReplyID = db.Column(db.Integer, primary_key=True)
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

    def serialize(self):
        d = Serializer.serialize(self)
        del d['article']
        del d['community']
        del d['user_info']
        del d['reply']
        d['writtenTime'] = str(d['writtenTime'])
        return d

class ReReplyRegion(db.Model):
    __tablename__ = 'rereply_region'

    reReplyID = db.Column(db.Integer, primary_key=True)
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

    def serialize(self):
        d = Serializer.serialize(self)
        del d['article']
        del d['community']
        del d['user_info']
        del d['reply']
        d['writtenTime'] = str(d['writtenTime'])
        return d

class ReReplyAll(db.Model):
    __tablename__ = 'rereply_all'

    reReplyID = db.Column(db.Integer, primary_key=True)
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

    def serialize(self):
        d = Serializer.serialize(self)
        del d['article']
        del d['community']
        del d['user_info']
        del d['reply']
        d['writtenTime'] = str(d['writtenTime'])
        return d
