# routes/open_dir_blueprint.py

from flask import Blueprint, request, jsonify
import os
from module.glode import glode
import logging

# 创建蓝图对象
openDirs_blueprint = Blueprint('openDirs_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@openDirs_blueprint.route('/openDirs', methods=['POST', 'GET'])
def openDirs():
    # 获取请求中的目录名
    dirs = request.args.get('OpenDirsName')

    # 检查目录是否存在
    if not dirs or not os.path.exists(dirs):
        logging.warning(f"请求的目录不存在: {dirs}")
        return jsonify({
            'url': 'openDirs',
            'data': [],
            'type': '失败',
            'message': '目录不存在或未提供'
        }), 400  # 返回400状态码

    try:
        # 列出目录中的文件和文件夹
        dir_list = os.listdir(dirs)
        logging.info(f"列出目录内容: {dir_list}")

        # 遍历当前目录的内容并筛选出文件夹
        folders = {index + 1: folder for index,
                   folder in enumerate(dir_list) if os.path.isdir(os.path.join(dirs, folder))}

        return jsonify({
            'url': 'openDirs',
            'data': dir_list,
            'type': '成功',
            'Time': glode.NowTime(),
            'dirName': dirs,
            'su': folders
        }), 200  # 返回200状态码

    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'url': 'openDirs',
            'data': [],
            'type': '失败',
            'message': '内部服务器错误',
            'error': str(e)
        }), 500  # 返回500状态码
