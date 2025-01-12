# routes/dir_blueprint.py

from flask import Blueprint, jsonify
import os
from module.glode import glode
from module.funtion.common import readdirpath
import logging

# 创建蓝图对象
OpenDir_blueprint = Blueprint('OpenDir_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@OpenDir_blueprint.route('/OpenDir', methods=['POST', 'GET'])
def OpenDir():
    try:
        # 获取当前目录
        current_dir = readdirpath.dirMOde(glode.dirpath())
        dir_list = os.listdir(current_dir)
        logging.info(f"当前目录中的文件和文件夹: {dir_list}")

        # 获取所有文件夹
        folders = {index: folder for index, folder in enumerate(dir_list) if os.path.isdir(os.path.join(current_dir, folder))}

        return jsonify({'su': folders, 'message': '获取文件夹成功'}), 200  # 返回200状态码

    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({'error': '内部服务器错误', 'message': str(e)}), 500  # 返回500状态码
