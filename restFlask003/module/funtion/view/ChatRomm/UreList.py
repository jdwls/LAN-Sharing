from flask import Blueprint, request, send_file, jsonify, make_response
import os
import shutil
from pathlib import Path
from flask_cors import CORS
import logging
import module.glode.glode as glode
import json
# 创建蓝图对象
UreList_blueprint = Blueprint('UreList_blueprint', __name__)
CORS(UreList_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


@UreList_blueprint.route('/Online_UreList', methods=['GET'])
def UreList():
    Urse_list=[]
    try:
        with open(glode.IsOlineNumbers(),'r',encoding='utf-8') as f:
            Online_Ures_json = json.load(f)
            f.close()
        with open(glode.AdminPathJson(),'r',encoding='utf-8') as f:
            AdminPath_json = json.load(f)
            f.close()
        for i in range(len(AdminPath_json)):
            Urse_list.append(AdminPath_json[i]['name'])
        with open(glode.UresPathJson(),'r',encoding="utf-8") as f:
            UresPath_json = json.load(f)
            f.close()
        for i in range(len(UresPath_json)):
            Urse_list.append(UresPath_json[i]['name'])   
        return jsonify({
            'code': 200,
            'msg': '获取成功',
            'data': Online_Ures_json,
            'UreList':Urse_list
        })
    except Exception as e:
        return jsonify({'code': 500, 'msg': e})
   