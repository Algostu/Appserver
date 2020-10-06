import os, sys, json, time
import hashlib
from tqdm import tqdm

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, grand_parent_dir)

from main.model import *
from baseDB import baseDB

class communityDB(baseDB):
    def __init__(self):
        super().__init__()
        # Todo : community ListUp
        self.all_communityList = ['자유', '질문']
        self.region_communityList = ['자유', '질문']
        self.school_communityList = ['자유', '질문']

    def register_all_communityList(self):
        for id in range(len(self.all_communityList)):
            if CommunityAll.query.filter_by(communityID=id).first():
                continue

            community_name = self.all_communityList[id]
            community = CommunityAll(communityID=id, communityName=community_name)
            db.session.add(community)
        db.session.commit()

    def load_regionList(self):
        regionInfo = RegionInfo.query.all()
        if not regionInfo:
            return []
        regionInfo = [r.regionID for r in regionInfo]
        return regionInfo

    def register_region_communityList(self):
        region_id_list = self.load_regionList()

        for region_idx in tqdm(range(len(region_id_list))):
            region_id = region_id_list[region_idx]
            for com_idx in range(len(self.region_communityList)):
                community_name = self.region_communityList[com_idx]
                community_id = com_idx + region_idx * 100 + region_id * 100
                if CommunityRegion.query.filter_by(communityID=community_id).first():
                    continue

                community = CommunityRegion(
                communityID=community_id, regionID= region_id, communityName=community_name)
                db.session.add(community)
        db.session.commit()

    def load_schoolList(self):
        schoolInfo = SchoolInfo.query.all()
        if not schoolInfo:
            return []
        schoolInfo = [r.schoolID for r in schoolInfo]
        return schoolInfo

    def register_school_communityList(self):
        school_id_list = self.load_schoolList()

        for school_idx in tqdm(range(len(school_id_list))):
            school_id = school_id_list[school_idx]
            for com_idx in range(len(self.school_communityList)):
                community_name = self.school_communityList[com_idx]
                community_id = com_idx*100 + school_idx * 10000
                if CommunitySchool.query.filter_by(communityID=community_id).first():
                    continue

                community = CommunitySchool(
                communityID=community_id, schoolID= school_id, communityName=community_name)
                db.session.add(community)
        db.session.commit()

    def run(self):
        self.register_all_communityList()
        self.register_region_communityList()
        self.register_school_communityList()
