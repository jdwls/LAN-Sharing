# routes/dir_blueprint.py

from flask import Blueprint, request, jsonify
import os
from module.glode import glode
import logging

# 创建蓝图对象
NewDir_blueprint = Blueprint('NewDir_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@NewDir_blueprint.route('/NewDir', methods=['POST', 'GET'])
def NewDir():
    # 获取新建文件夹的名字和路径
    NewDirName = request.args.get('NewDirName')
    NewDirPath = request.args.get('NewDirPath')

    try:
        # 检查输入参数
        if not NewDirName or not NewDirPath:
            logging.warning("文件夹名称或路径未提供")
            return jsonify({
                'url': 'NewDir',
                'status': 'error',
                'message': '文件夹名称或路径未提供',
                'Time': glode.NowTime()
            }), 400  # 返回400状态码

        # 检查目录是否已经存在
        if os.path.exists(os.path.join(NewDirPath, NewDirName)):
            logging.info(f"文件夹已经存在: {os.path.join(NewDirPath, NewDirName)}")
            return jsonify({
                'url': 'NewDir',
                'status': 'error',
                'message': '文件夹已经存在',
                'Time': glode.NowTime()
            }), 409  # 返回409状态码

        # 创建新目录
        os.makedirs(os.path.join(NewDirPath, NewDirName))
        logging.info(f"成功创建文件夹: {os.path.join(NewDirPath, NewDirName)}")

        # 记录操作日志
        with open(glode.dirPathLog(), 'a', encoding="utf-8") as f:
            f.write(
                f"{glode.NowTime()} 新建文件夹: {os.path.join(NewDirPath, NewDirName)}\n")

        # 返回成功信息
        return jsonify({
            'url': 'NewDir',
            'status': 'success',
            'message': '文件夹创建成功',
            'Time': glode.NowTime()
        }), 201  # 返回201状态码

    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'url': 'NewDir',
            'status': 'error',
            'message': '内部服务器错误',
            'details': str(e),
            'Time': glode.NowTime()
        }), 500  # 返回500状态码
