import module.glode.glode as glode
from flask import  jsonify
import json
import time
def isAdminAndUrsejsonData(Time,Name):
    DATETIME=60*60*24*1000
    try:
        with open(glode.AdminPathJson(),'r',encoding='utf-8') as f:
            AdminjsonData = json.load(f)
            f.close()
        with open(glode.UresPathJson(), 'r', encoding='utf-8') as f:
            UserjsonData = json.load(f)
            f.close()
    except Exception as e:
        return jsonify(
            {'Time': Time},
            {'message':e})
    try:
        for i in range(len(AdminjsonData)):
            if AdminjsonData[i]['name']==Name:
                return jsonify(
                    {'Time': Time},
                    {'message':"时间戳存在"})
        for i in range(len(UserjsonData)):
            if UserjsonData[i]['name']==Name and UserjsonData[i]['Time']==Time:
                    if int(round(time.time() * 1000))-int(Time)<DATETIME:
                        return jsonify(
                            {'Time': Time},
                            {'message':"用户存在"})   
        return jsonify( 
            {'Time': Time},
            {'message':'用户不存在'})
    except Exception as e:
        return jsonify(
            {'Time': Time},
            {'message':e})