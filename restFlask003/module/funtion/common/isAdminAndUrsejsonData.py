import module.glode.glode as glode
from flask import  jsonify
import json
import time
def isAdminAndUrsejsonData(Time,Name):
    URESDATETIME=60*60*24*1000
    ADMINDATETIME=60*60*8*1000
    try:
        with open(glode.AdminPathJson(),'r',encoding='utf-8') as f:
            AdminjsonData = json.load(f)
            f.close()
        with open(glode.UresPathJson(), 'r', encoding='utf-8') as f:
            UserjsonData = json.load(f)
            f.close()
    except Exception as e:
        return e
    try:
        for i in range(len(AdminjsonData)):
            if AdminjsonData[i]['name']==Name and AdminjsonData[i]['Time']==Time:
                 if int(round(time.time() * 1000))-int(Time)<ADMINDATETIME:
                        return "用户存在" 
        for i in range(len(UserjsonData)):
            if UserjsonData[i]['name']==Name and UserjsonData[i]['Time']==Time:
                    if int(round(time.time() * 1000))-int(Time)<URESDATETIME:
                        return "用户存在"   
        return '用户不存在'
    except Exception as e:
        return e