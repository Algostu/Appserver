import os, sys, json, time
import hashlib
from tqdm import tqdm

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, grand_parent_dir)

from main.model import *
from baseDB import baseDB
from univ_info import convert_to_json

class univDB(baseDB):
    def __init__(self):
        super().__init__()
        self.eduPage = {"아주대학교" : "http://www.iajou.ac.kr/ipsi/board/notice/list.do",
            "수원대학교" : "https://ipsi.suwon.ac.kr/index.html?menuno=2084",
            "경희대학교" : "https://iphak.khu.ac.kr/cop/bbs/selectBoardList.do",
            "성균관대학교" : "https://admission.skku.edu/connect/dataroom.htm?ctg_cd=susi",
            "경기대학교" : "http://enter.kyonggi.ac.kr/cms/FR_CON/index.do?MENU_ID=210",
            "수원여자대학교" : "https://entr.swwu.ac.kr/cop/bbs/BBSMSTR_000000000051/selectBoardList.do?mn=ko"
        }
        self.base_url = "http://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=9916c8aba361af331c611caf582ad148&svcType=api&svcCode=MAJOR_VIEW&contentType=json&gubun=univ_list&univSe=univ&majorSeq="

    def register_UnivInfo(self):
        db.session.query(UnivInfo).delete()
        db.session.commit()
        univ_info = convert_to_json('crawler/data/대학교 목록.xlsx', 'crawler/data/dobie.xlsx')
        for univ in tqdm(univ_info):
            unit = UnivInfo(univName=univ['name'], subRegion=univ['sub_region'], homePage=univ['homePage'],
            engname=univ['eng_name'], youtube=univ.pop('youtube', ""), admission=univ.pop('admission', ""))
            # eduPage = self.eduPage.pop(univ['name'], "")
            # unit.eduHomePage = eduPage
            # unit.logoPossible = 1 if eduPage != '' else 0
            db.session.add(unit)
        db.session.commit()

    def register_major(self):
        db.session.query(MajorInfo).delete()
        db.session.commit()
        major_infos = self.read_json("crawler/data/major_info.json")["dataSearch"]["content"]
        for major in tqdm(major_infos):
            try:
                detail_info = self.get_json(self.base_url+str(major['majorSeq']))['dataSearch']['content'][0]['chartData'][0]
                gender = ""
                employment_rate = ""
                avg_salary = ""
                if "gender" in detail_info:
                    gender = detail_info['gender'][0]['data'] + ":" + detail_info['gender'][1]['data']
                if "employment_rate" in detail_info:
                    employment_rate = detail_info['employment_rate'][0]['data']
                if "avg_salary" in detail_info:
                    avg_salary = detail_info['avg_salary'][0]['data']
                unit = MajorInfo(majorSeq=major['majorSeq'], mClass=major['mClass'],
                gender=gender,employment_rate=employment_rate,avg_salary=avg_salary)
                db.session.add(unit)
                db.session.commit()
            except:
                print(major)

    def run(self):
        # self.register_major()
        self.register_UnivInfo()
