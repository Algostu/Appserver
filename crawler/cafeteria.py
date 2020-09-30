import requests
import json
import time
from tqdm import tqdm
from baseCrawler import crawler

class cafeteriaCrawler(crawler):
    def __init__(self):
        super().__init__('https://www.foodsafetykorea.go.kr/')

    def get_list(self):
        url = 'portal/sensuousmenu/selectSchoolMeals_school.do'
        data = {}
        school_list = self.parse_school_info(self.post_url(url, json.dumps(data))['list'])
        return school_list

    def parse_school_info(self, schools):
        region_school = {}
        for school in schools:
            if school['ara'] not in region_school:
                region_school[school['ara']] = []

            if '고등학교' in school['schl_nm']:
                region_school[school['ara']].append({'id':school['schl_cd'], 'name':school['schl_nm']})
        return region_school

    def parse_menu(self, menu_data):
        menus = []
        for raw_menu in menu_data['list']:
            if "dd_date" not in raw_menu or "lunch" not in raw_menu:
                continue

            menus.append({
                'date' : raw_menu['dd_date'],
                'week' : raw_menu['week_dvs'],
                'week_day' : raw_menu['week_day'],
                'lunch' : raw_menu['lunch'],
            })

        return menus

    def get_json(self):
        url = 'portal/sensuousmenu/selectSchoolMonthMealsDetail.do'
        school_list = self.get_list()

        cafe_menu_per_school = {}

        for region, schools in tqdm(school_list.items()):
            region_school = {}
            for school in tqdm(schools):
                time.sleep(0.01)
                post_data = {
                    'schl_cd' : school['id'],
                    'type_cd' : 'M',
                    'year' : '2020',
                    'month' : '9',
                }

                menus = self.parse_menu(self.post_url(url, post_data))
                region_school[school['name']] = menus

            cafe_menu_per_school[region] = region_school

        self.save_json('cafeteria_menu_per_school', cafe_menu_per_school)
        self.save_json('school_list', school_list)




if __name__ == '__main__':
    api = cafeteriaCrawler()
    api.get_json()
