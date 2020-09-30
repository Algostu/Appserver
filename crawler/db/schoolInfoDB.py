import os, sys, json, time
import hashlib
from tqdm import tqdm

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, grand_parent_dir)

from main.model import *
from baseDB import baseDB

class schoolDB(baseDB):
    def __init__(self):
        super().__init__()

    def register_regionInfo(self):
        for name, code in self.regionInfo.items():
            # if exist already, skip it
            if RegionInfo.query.filter_by(regionID=code).first():
                continue
            region = RegionInfo(regionID=code, regionName=name)
            db.session.add(region)
        db.session.commit()

    def register_schoolInfo(self):
        school_info = self.read_json(parent_dir + '/data/school_info.json')
        for schools in school_info.values():
            for sch in tqdm(schools):
                id = int(hashlib.sha224("".join([sch[item] for item in self.hash_item]).encode('utf-8')).hexdigest(), 16) % (10 ** 9)
                regionID = self.regionInfo[self.nickName_to_realName[sch['region']]]
                gender = self.gender[sch['gender']]
                if SchoolInfo.query.filter_by(schoolID = id).first():
                    continue
                school = SchoolInfo(schoolID=id, regionID=regionID,
                schoolName=sch['name'], gender=gender,
                contact=sch['contact'], homePage=sch['homePage'])
                db.session.add(school)
            db.session.commit()

    def show_schoolInfo(self):
        for row in SchoolInfo.query.all():
            print(row)

    def run(self):
        self.register_regionInfo()
        self.register_schoolInfo()
