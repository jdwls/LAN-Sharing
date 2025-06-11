from flask import Blueprint, request, send_file, jsonify, make_response
import os
import shutil
from pathlib import Path
from flask_cors import CORS
import logging
import json
import module.funtion.common.isAdminAndUrsejsonData as isAdminAndUrsejsonData
# 创建蓝图对象
Toker_blueprint = Blueprint('Toker_blueprint', __name__)
CORS(Toker_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
@Toker_blueprint.route('/Toker', methods=['GET'])
def Toker():
    Time = request.args.get('Time')
    Name=request.args.get('Name')
    if Time ==None and Name ==None:
        return jsonify(
            {'Time': Time},
            {'message':'出现问题'})
    return isAdminAndUrsejsonData.isAdminAndUrsejsonData(Time,Name)

  
    
  
