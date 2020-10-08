import os, sys, json, time, datetime
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
        now = time.localtime()
        time_format = "%04d/%02d/%02d %02d:%02d:%02d"
        self.version = time_format % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        self.month = now.tm_mon
        self.year = now.tm_year
        self.day = now.tm_mday

    def register_cafeInfo(self):
        # Todo: fix processe_cafeteria.json -> cafeteria.json
        cafe_info = self.read_json(parent_dir + '/data/'+str(self.year)+'-'+str(self.month)+'-'+'cafeteria_menu_per_school.json')

        for region, schools in cafe_info.items():
            regionName = region[:-3]
            regionID = self.regionInfo[regionName]
            for schoolName, menus in tqdm(schools.items()):
                school_infos = SchoolInfo.query.filter_by(schoolName=schoolName, regionID=regionID).first()
                if not school_infos:
                    continue
                # case 1 : there is no school info in info table
                # case 2 : already exists
                # Todo : find if case 3 exist
                # case 3 : if there is same named school in same region (1개 누락)
                for info in CafeteriaInfo.query.filter_by(schoolID=school_infos.schoolID).all():
                    if info.version.year != self.year:
                        if self.month + 12 -2 > info.version.month:
                            db.session.delete(info)
                    else:
                        if self.month -2 > info.version.month:
                            db.session.delete(info)
                        if self.month == info.version.month and self.day != info.version.day:
                            db.session.delete(info)

                cafe = CafeteriaInfo(schoolID=school_infos.schoolID, regionID=regionID, version=self.version, cafeMenu=json.dumps(menus, indent=4, ensure_ascii=False))
                db.session.add(cafe)
        db.session.commit()

    def test_cafeinfo(self):
        cafe = CafeteriaInfo.query.first()
        print(json.loads(cafe.cafeMenu, encoding="utf-8"))

    def run(self):
        self.register_cafeInfo()
        # self.test_cafeinfo()
