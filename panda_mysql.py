import pandas as pd
import mysql.connector
import numpy as np

mysql_cn = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='db')


query_list = [
    #  'select count(*) from db.Chicago_Crime',
    #  'select * from db.Chicago_Crime  limit 10'
    #  'select count(*) from db.Chicago_Crime where ARREST = \'True\'',
    #  'select distinct(PRIMARY_TYPE) from db.Chicago_Crime where Location_Description = "GAS STATION"'
    #  'select distinct(`COMMUNITY AREA NAME`) from db.Census_Data where `COMMUNITY AREA NAME` like \'B%\''
    #  'select'select avg(Safety_Score) from db.Chicago_Public_Schools' distinct(NAME_OF_SCHOOL) from db.Chicago_Public_Schools where  HEALTHY_SCHOOL_CERTIFIED= \'Yes\'',
    #  'select avg(College_Enrollment) from db.Chicago_Public_Schools',
    #  'select distinct(Community_Area_Number) from db.Chicago_Public_Schools where COLLEGE_ENROLLMENT>568'
    #  'SELECT distinct(COMMUNITY_AREA_NUMBER) FROM db.Chicago_Public_Schools where SAFETY_SCORE<15',
     'select distinct(`PER CAPITA INCOME`) from db.Census_Data as cd Inner join db.Chicago_Public_Schools as cps on cd.`Community Area Number`=cps.Community_Area_Number where cps.SAFETY_SCORE=1',

]







cnt=0
for query in query_list:
    cnt = cnt + 1
    result = pd.read_sql(query , con=mysql_cn)   
    print("Question " + str(cnt) +"==>" + query)
    print(str(result))

mysql_cn.close()                             