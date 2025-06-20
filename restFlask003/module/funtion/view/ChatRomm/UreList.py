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


@UreList_blueprint.route('/UreList', methods=['GET'])
def UreList():
    try:
        with open(glode.AdminPathJson(),'r',encoding='utf-8') as f:
            AdminjsonData = json.load(f)
            f.close()
        with open(glode.UresPathJson(), 'r', encoding='utf-8') as f:
            UserjsonData = json.load(f)
            f.close()
    except Exception as e:
        return jsonify({'code': 500, 'msg': e})
    try:
        data = []
        for i in range(len(AdminjsonData)):
            data.append(AdminjsonData[i]['name'])
        for i in range(len(UserjsonData)):
            data.append(UserjsonData[i]['name'])
        return jsonify({'code': 200, 'msg': '获取成功', 'data': data})
    except Exception as e:
        return jsonify({'code': 500, 'msg': e})