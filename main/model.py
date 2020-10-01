# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect


db = SQLAlchemy()

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class Article(db.Model):
    __tablename__ = 'article'

    articleID = db.Column(db.Integer, primary_key=True)
    communityID = db.Column(db.ForeignKey('community.communityID', ondelete='CASCADE'), index=True)
    userID = db.Column(db.ForeignKey('user_info.userID'), index=True)
    isAnonymous = db.Column(db.Integer)
    title = db.Column(db.String(50, 'utf8_unicode_ci'))
    content = db.Column(db.String(5000, 'utf8_unicode_ci'))
    viewNumber = db.Column(db.Integer, server_default=db.FetchedValue())
    reply = db.Column(db.Integer, server_default=db.FetchedValue())
    heart = db.Column(db.Integer, server_default=db.FetchedValue())
    writtenTime = db.Column(db.DateTime)

    community = db.relationship('Community', primaryjoin='Article.communityID == Community.communityID', backref='articles')
    user_info = db.relationship('UserInfo', primaryjoin='Article.userID == UserInfo.userID', backref='articles')



class Community(db.Model):
    __tablename__ = 'community'

    communityID = db.Column(db.Integer, primary_key=True)
    communityName = db.Column(db.String(20, 'utf8_unicode_ci'))



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

    userID = db.Column(db.BigInteger, primary_key=True)
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
