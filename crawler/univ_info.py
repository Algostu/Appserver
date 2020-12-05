import openpyxl
import json
import os
from tqdm import tqdm
import re

def convert_to_json(path1, path2):
    # 엑셀파일 열기
    wb = openpyxl.load_workbook(path1)
    wb2 = openpyxl.load_workbook(path2)
    # 현재 Active Sheet 얻기
    ws = wb.active
    ws2 = wb2.active
    dobie = {}
    for r in tqdm(ws2.rows):
        if not r[1].value:
            continue
        dobie[r[1].value] = {"admission":r[3].value, "youtube":r[4].value}

    high_school_data = []
    # logo
    # kor_to_eng = {}
    for r in tqdm(ws.rows):
        if r[0].row  < 6 or r[1].value not in ['대학교', '각종대학(대학)', '교육대학', '전공대학', '전문대학(4년제)']:
            continue
        row_dict = {
            "school_type":r[1].value,
            "region":r[2].value,
            "sub_region":r[3].value,
            "name":r[4].value,
            "eng_name":re.sub("-|&", "_", "_".join(r[5].value.split(" ")).lower()),
            "foundation":r[8].value,
            "homePage":r[13].value
        }
        # logo
        # converted_name = row_dict['name'].split(" ")[0]
        # kor_to_eng[converted_name] = row_dict['eng_name']

        if r[4].value in dobie:
            row_dict.update(dobie[r[4].value])
        high_school_data.append(row_dict)

    # logo
    # base_path = './crawler/data/logo/'
    # file_list = os.listdir(base_path)
    # dst = ""
    # for name in file_list:
    #     src = os.path.join(base_path, name)
    #     file_name, ext = name.split(".")
    #     conv_name = file_name.split("_")[0].split(" ")[0]
    #     if "대학교" not in conv_name:
    #         conv_name += "학교"
    #     if conv_name == '아세아연합신학대학교':
    #         dst = conv_name = "asia_united_theological_university"
    #     else:
    #         dst = kor_to_eng[conv_name]
    #     dst = os.path.join(base_path, dst+"."+ext)
    #     os.rename(src, dst)


    return high_school_data
# univ_info = convert_to_json('crawler/data/대학교 목록.xlsx', 'crawler/data/dobie.xlsx')
# if __name__ == '__main__':
#     //analyze()
