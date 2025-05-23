# routes/dir_blueprint.py

from flask import Blueprint, request, jsonify
from module.glode import glode  # 自定义模块
from module.funtion.common import readdirpath  # 假设 readdirpath 也是自定义模块
import os
import logging

# 创建蓝图对象
SucceedselectedDir_blueprint = Blueprint(
    'SucceedselectedDir_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@SucceedselectedDir_blueprint.route('/SucceedselectedDir', methods=['POST', 'GET'])
def SucceedselectedDir():
    # 从请求参数中获取路径
    dirname = request.args.get('dirname')

    if not dirname:  # 检查 dirname 是否存在
        logging.warning("未提供目录名")
        return jsonify({
            'url': 'SucceedselectedDir',
            'data': None,
            'type': '失败',
            'message': '未提供目录名',
            'Time': glode.NowTime()
        }), 400  # 返回400状态码

    logging.info(f"确认路径: {dirname}")

    try:
        # 将路径写入文件
        with open(glode.dirpath(), 'w', encoding="utf-8") as f:
            f.write(dirname)

        # 将日志写入文件
        with open(glode.dirPathLog(), 'a', encoding="utf-8") as f:
            log_entry = f"{glode.NowTime()}  确定路径: {readdirpath.dirMOde(glode.dirpath())}\n"
            f.write(log_entry)

        return jsonify({
            'url': 'SucceedselectedDir',
            'data': readdirpath.dirMOde(glode.dirpath()),
            'type': '确定路径',
            'Time': glode.NowTime()
        }), 200  # 返回200状态码

    except Exception as e:
        logging.error(f"写入目录路径或日志时发生错误: {e}")
        return jsonify({
            'url': 'SucceedselectedDir',
            'data': None,
            'type': '失败',
            'message': '保存路径时出错',
            'Time': glode.NowTime()
        }), 500  # 返回500状态码
