import os, sys

dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(dir)
grand_parent_dir = os.path.dirname(parent_dir)
sys.path.insert(0, dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, grand_parent_dir)

from flask_script import Command, Manager, Option

from schoolInfoDB import schoolDB
from cafeteriaDB import cafeDB
from communityDB import communityDB
from contestDB import contestDB
from univDB import univDB
from survey import surveyDB

class dbAdapter(Command):
    option_list = (
        Option('--type', '-T', dest='type', default=None),
    )

    def run(self, type):
        if type=='schoolInfo' or type=='S':
            schoolInfo = schoolDB()
            schoolInfo.run()
        elif type=='cafeInfo' or type=='C':
            cafe = cafeDB()
            cafe.run()
        elif type=='initialCommunity' or type=='I':
            community = communityDB()
            community.run()
        elif type=='contest' or type=='T':
            contest = contestDB()
            contest.run()
        elif type=='univ' or type=='U':
            univ = univDB()
            univ.run()
        elif type=="alarm" or type=="A":
            survey = surveyDB()
            survey.run()
            
