import os, sys, json, time, datetime
import hashlib
from tqdm import tqdm

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, grand_parent_dir)

from main.model import *
from main.extensions import *
from baseDB import baseDB
from contestCrawler import contestCrawler

class surveyDB(baseDB):
    def __init__(self):
        super().__init__()
        now = time.localtime()
        time_format = "%04d/%02d/%02d"
        self.version = time_format % (now.tm_year, now.tm_mon, now.tm_mday)
        self.month = now.tm_mon
        self.year = now.tm_year
        self.day = now.tm_mday

    def run(self):
        title = "설문조사를 해주세요."
        body = {"communityType":0, "articleID":13684, "communityID":3,
        "content":"설문조사를 진행해주세요.", "time":get_cur_date(), "type":0}
        users = UserInfo.query.all()
        for user in users:
            fcm_token = user.fcmToken
            send_push_alarm(fcm_token, title, json.dumps(body))
