import os, sys, json, time
import hashlib
from tqdm import tqdm

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, grand_parent_dir)

from main.model import *
from baseDB import baseDB

class cafeDB(baseDB):
    def __init__(self):
        super().__init__()

    def register_cafeInfo(self):
        # Todo: fix processe_cafeteria.json -> cafeteria.json
        cafe_info = self.read_json(parent_dir + '/data/processed_cafeteria_menu_per_school.json')

        for region, schools in cafe_info.items():
            regionName = region[:-3]
            regionID = self.regionInfo[regionName]
            for schoolName, menus in schools.items():
                info = SchoolInfo.query.filter_by(schoolName=schoolName, regionID=regionID).first()
                # case 1 : there is no school info in info table
                # case 2 : already exists
                # Todo : find if case 3 exist
                # case 3 : if there is same named school in same region
                if not info or CafeteriaInfo.query.filter_by(schoolID=info.schoolID).first():
                    continue
                cafe = CafeteriaInfo(schoolID=info.schoolID, regionID=regionID, cafeMenu=json.dumps(menus))
                db.session.add(cafe)
        db.session.commit()

    def run(self):
        self.register_cafeInfo()
