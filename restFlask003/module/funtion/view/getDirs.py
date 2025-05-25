# routes/file_blueprint.py

from flask import Blueprint, request, jsonify
import os
import shutil
from module.glode import glode
from ..common.readdirpath import dirMOde
import logging

# 创建蓝图对象
getDirs_blueprint = Blueprint('getDirsblueprint ', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@getDirs_blueprint.route('/getDirs', methods=['GET'])
def getDirs():
    print(dirMOde(glode.dirpath()))
    return jsonify({
        'error': '正确',
        'data': str(dirMOde(glode.dirpath()))
    }), 200  # 返回500状态码
