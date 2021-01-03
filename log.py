import re
import json
import string
import datetime
import random
import pandas as pd
from tqdm import tqdm
import openpyxl

def save_json(file_name, json_data):
    with open('log/'+file_name+'.json', "w", encoding = 'utf8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

ip_pattern = re.compile("((?:[0-9]+\\.){3}(?:[0-9]+))")
date_time_pattern = re.compile("[0-9]+/[a-zA-Z]+/2020 [0-9]+:[0-9]+:[0-9]+")
method_pattern = re.compile("(?:GET|POST) /(.*) HTTP")

total_access = []
ip_per_freq = {}
date_per_freq = {}
time_per_freq = {}
page_per_freq = {}
letters_and_digits = string.digits

with open("nohup.out", "r", encoding='utf-8') as f:
    for line in tqdm(f.readlines()):
        ip_matched = ip_pattern.search(line)
        date_matched = date_time_pattern.search(line)
        method_matched = method_pattern.search(line)
        if ip_matched and date_matched and method_matched:
            ip = ip_matched.group(0).replace(".", "")
            date = date_matched.group(0)
            url_header = method_matched.group(1)
            # update total access
            total_access.append({"ip":ip, "date":date, "url":url_header})
            # update ip data
            if ip not in ip_per_freq:
                ip_per_freq[ip] = []
            ip_per_freq[ip].append({"date":date, "url":url_header})
            # update method data
            method = url_header.split("/")[0].split("?")[0]
            if method not in page_per_freq:
                page_per_freq[method] = 0
            page_per_freq[method] += 1
            # update time and date data
            date, time = date.split(" ")
            time = time.split(":")[0]
            if date not in date_per_freq:
                date_per_freq[date] = {}
            if method not in date_per_freq[date]:
                date_per_freq[date][method] = 0
            date_per_freq[date][method] += 1
            if time not in time_per_freq:
                time_per_freq[time] = {}
            if method not in time_per_freq[time]:
                time_per_freq[time][method] = 0
            time_per_freq[time][method] += 1
    # masking ip_per_freq.json
    temp = {}
    for key, val in ip_per_freq.items():
        random_str = ''.join((random.choice(letters_and_digits) for i in range(2)))
        random_key = key + random_str
        temp[random_key] = val
    ip_per_freq = temp
    ip_freq = {key:len(val) for key, val in temp.items()}
    freq_ip = {}
    for ip, freq in ip_freq.items():
        if freq > 0 and freq <= 5:
            freq = 5
        elif freq > 5 and freq <= 10:
            freq = 10
        elif freq > 10 and freq <= 50:
            freq = 50
        elif freq > 50 and freq <= 100:
            freq = 100
        elif freq > 100 and freq <= 500:
            freq = 500
        elif freq > 500 and freq <= 1000:
            freq = 1000
        elif freq > 1000:
            freq = 2000
        if freq not in freq_ip:
            freq_ip[freq] = 0
        freq_ip[freq] += 1
    freq_ip = [{"access":access, "access num": str(access), "user": freq} for access, freq in freq_ip.items()]
    # preparing data_per_freq.json
    date_per_freq_list = []
    functionalities = ["article", "auth", "search", "admin", "login", "mypage", "cafeteria", "reply", "contest", "univ"]
    for key, val in date_per_freq.items():
        row = {"date":key}
        for function in functionalities:
            row[function] = val.pop(function, 0)
        date_per_freq_list.append(row)
    date_per_freq_list.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%d/%b/%Y'))
    # preparing time_per_freq.json
    time_per_freq_list = []
    for key, val in time_per_freq.items():
        row = {"time":key}
        for function in functionalities:
            row[function] = val.pop(function, 0)
        time_per_freq_list.append(row)
    # perparing page_per_freq.json
    page_per_freq_list = [{fname:page_per_freq[fname] for fname in functionalities}]
    # pd.DataFrame(total_access).to_excel('log/total_access.xlsx', index=False)
    # pd.DataFrame(freq_ip).to_excel('log/freq_ip.xlsx', index=False)
    # pd.DataFrame(date_per_freq_list).to_excel('log/date_per_freq_list.xlsx', index=False)
    # pd.DataFrame(time_per_freq_list).to_excel('log/time_per_freq_list.xlsx', index=False)
    # pd.DataFrame(page_per_freq_list).to_excel('log/page_per_freq_list.xlsx', index=False)

    save_json('total_access', total_access)
    save_json('ip_per_freq', ip_per_freq)
    save_json('freq_ip', freq_ip)
    save_json('date_per_freq', date_per_freq)
    save_json('time_per_freq', time_per_freq)
    save_json('page_per_freq', page_per_freq)
