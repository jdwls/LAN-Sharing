# routes/top_level_directory_blueprint.py
from flask import Blueprint, request, jsonify
from module.glode import glode
import os
import logging
import module.funtion.common.readdirpath as readdirpath
# 创建蓝图对象
TopLevelDirectory_blueprint = Blueprint(
    'TopLevelDirectory_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@TopLevelDirectory_blueprint.route('/TopLevelDirectory', methods=['POST', 'GET'])
def TopLevelDirectory():
    TopLevelDirectoryPathName = request.args.get('TopLevelDirectoryPathName')
    TopLevelDirectoryPathNameSplit = TopLevelDirectoryPathName.split('/')
    if not TopLevelDirectoryPathName:  # 检查是否提供路径
        logging.warning("未提供TopLevelDirectoryPathName")
        return jsonify({
            'url': 'TopLevelDirectory',
            'data': None,
            'type': '失败',
            'message': '未提供路径',
            'Time': glode.NowTime(),
        }), 400  # 返回400状态码
    elif len(TopLevelDirectoryPathNameSplit)==1:
        logging.info(f"请求的路径是顶层路径: {TopLevelDirectoryPathName}")
        return jsonify({
            'url': 'TopLevelDirectory',
            'data': TopLevelDirectoryPathNameSplit,
            'type': '失败',
            'message': '顶层目录无法返回',
            'Time': glode.NowTime(),
        }), 400  # 返回400状态码
    # 处理路径
    elif TopLevelDirectoryPathName == readdirpath.dirMOde(glode.dirpath()):
        logging.info(f"处理路径: {TopLevelDirectoryPathName}")
        logging.info(f"处理路径: {readdirpath.dirMOde(glode.dirpath())}")
        return jsonify({
            'url': 'TopLevelDirectory',
            'data': None,
            'type': '失败',
            'message': '路径与根目录相同,无法返回',
            'Time': glode.NowTime(),
        }), 400  # 返回400状态码
    else:
        result=''
        for i in range(len(TopLevelDirectoryPathNameSplit)-1):
            result = result+TopLevelDirectoryPathNameSplit[i] + '/'
            print(i)
            print(TopLevelDirectoryPathNameSplit[i])
        return jsonify({
            'url': 'TopLevelDirectory',
            'data': result,
            'type': '成功',
            'Time': glode.NowTime(),
        }), 200  # 返回200状态码
