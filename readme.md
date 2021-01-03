# App Server Read Me

<p align="center">
<img width="200" alt="logo" src="https://github.com/Algostu/dodam-appserver/blob/master/log/logo.png?raw=true">
</p>
<h4 align="center">mobile online community application server</h4>
</p>
<p align="center">
	<a href="https://travis-ci.com/Algostu/Appserver">
		<img src="https://travis-ci.com/Algostu/Appserver.svg?token=G8pVCbCauf3DdVpT6k6s&branch=master"/>
	</a>
	<a href="https://codecov.io/gh/Algostu/Appserver">
		<img src="https://codecov.io/gh/Algostu/Appserver/branch/master/graph/badge.svg?token=Q60ZB3RKIR"/>
	</a>
	<a href="https://play.google.com/store/apps/details?id=com.dum.dodam">
	    	<img src="https://img.shields.io/badge/download-57-1EAEDB"
		 alt="download">
	</a>
	<a href="https://play.google.com/store/apps/details?id=com.dum.dodam">
	  	<img src="https://img.shields.io/badge/user-40-ff69b4"
		 alt="user">
	</a>
</p>

<p align="center">
  <a href="#service-history-analysis">service history</a> • 
  <a href="#service-history-analysis">service architecture</a> • 
  <a href="#tutorial">tutorial</a> •  
  <a href="#options">option</a> •   
  <a href="#file-structure">File Structure</a> • 
  <a href="#related">Related</a> • 
  <a href="#license">License</a>
</p>

<p align="center">
This is dodam-dodam application's app server repository. Application's app repo is <a href="https://github.com/Algostu/dodam-android">here</a>
Dodam-dodam is mobile onlie communication application for highschool student. We develop this app during 2020 fall semester ajou univ's captsone design class.(X283)
This application is actually serviced to customer for about 2 months and about 80 customer installed and use our app. When we close our app down, the number of member of system is about 50. 
</p>

## Service History Analysis

We upload our app to play store and some kind customer come and use our app. Now we want to analysis how our service work during short service time. Our service start at 12th October and end at 30th December. The number of total customer of our system is 48 and About 80 people install our app via playstore. Now our app is not available to download on play store. Overview of our user download history is below graph. You can check more detail analysis [here](https://github.com/Algostu/dodam-appserver/blob/master/docs/log_analysis.md)

![history](https://raw.githubusercontent.com/Algostu/dodam-appserver/master/log/history.png)

## Service Architecture 

Main Architecture of dodam service is client-server. And issues we conflict during development are recorded [here](https://github.com/Algostu/dodam-appserver/blob/master/docs/service_issues.md).

![architecture](https://github.com/Algostu/dodam-appserver/blob/master/log/service%20architecture.png)

## Tutorial 

You should download python 3.5 and other related program. Beacause I did not know about docker at that time, I can not provide docker file, sorry.

- python 3.5
- mysql
- redis
- apache (for production)

If you install all required program to your development environment, clone or download source code from github. After download source code, please download required python package. You can download required package in `requirements.txt`

```bash
git clone https://github.com/Algostu/dodam-appserver.git
pip install -r "requirements.txt"
```

You can start server by simple command

```bash
python manage.py runserver 
```

## Options

You can initialize and migrate to database using flask-alchemy migration command

```bash
python manage.py db migrate
python manage.py db upgrade
```

You can insert data into database using `cralwer` option 

```bash
python manage.py crawler -T [option]
```

crawler option list

```python
if type=='schoolInfo' or type=='S': # highschool info list
	schoolInfo = schoolDB()
	schoolInfo.run()
elif type=='cafeInfo' or type=='C': # article of community  
	cafe = cafeDB()
	cafe.run()
elif type=='initialCommunity' or type=='I': # initialize community
	community = communityDB()
	community.run()
elif type=='contest' or type=='T': # insert crawlered contest data into db
	contest = contestDB()
	contest.run()
elif type=='univ' or type=='U': # insert data suc as university name, youtube link, etc 
	univ = univDB()
	univ.run()
elif type=="alarm" or type=="A": # send user notification 
	survey = surveyDB()
	survey.run()
```

## File Structure  

1. `main/`
  - `__init__.py` : App factory. This file load required package and apply to app module.
  - `view.py` : If you want to add new app, pls add your blue print here.
  - `config.py` : This is configuration file. Configuration file contain 3 versions : dev, test, production. Each mode of configuration have different server configuration.
  - `model.py` : ORM based database schema made using flask-sqlalchemy library.
  - `extention.py` : This is kind of utility function used in this project. We collect most frequently used utilities to this module. 

2. `api_folder_name/`

   Each folder contain only `view.py`. This file contain api function. 

   `api_folder_name` list

   1. admin : API for web page. Web page's main functionality is to give maintainers to manage user and grant user access to our app.
   2. article : This module contain api related to article, which user write, read, delete. User use this api to load hot article list and recent article list. 
   3. cafeteria : This api does not used anymore. Our cafeteria api is replaced by public api officially supported by Office of Education.
   4. contest : We provide contest info targeting high school student. We collect this data from other web site. 
   5. login : This is related to authentication : Login, Logout, Sign-up, Sign-out. FCM-token, etc.
   6. mypage : Provide survey link to user.
   7. replys : This APIs are used for CRUD reply of article. 
   8. search : This module contain univ list search, major list search and high school list search.
   9. univ : Currently used api is live-show api. Other APIs are not used or replaced now.

3. `test/`

    We use pytest to test module. This test module originally contain test case operated in testing server. But currently no testing server is alive. We comment out test case.

4. `crawler/`

     Our data got from other site and needed to refined to use in our database. Each module in `cralwer` is crawler bring data from other website.

     Under `db` folder, we made database related module. Each module are made for creating, initializing data base and load data and inset it into table. To use this function, you should turn off `STRICT_TRANS_TABLES` option in your mysql setting.

5. `docs` 

   Documents made for myself to reference in the future.

## Related

* [dodam-android](https://github.com/Algostu/dodam-android) : 도담도담 android

* [도담도담](https://play.google.com/store/apps/details?id=com.dum.dodam) : 도담도담 play store
* [d.___.dam](https://www.instagram.com/d.___.dam/) : 도담도담 인스타그램

## License

This application is freely available for free non-commercial use, and may be redistributed under these conditions. Please, see the [license](LICENSE) for further details.

