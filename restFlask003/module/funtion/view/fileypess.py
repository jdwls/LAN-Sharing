# routes/fileypess_blueprint.py

from flask import Blueprint, request, jsonify
from module.glode import glode
import logging

# 创建蓝图对象
fileypess_blueprint = Blueprint('fileypess_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@fileypess_blueprint.route('/fileypess', methods=['POST', 'GET'])
def fileypess():
    ViewButtonOfficEword = request.args.get('ViewButtonOfficEword')
    print(ViewButtonOfficEword,'---------------------------------------------')
    try:
        # 确保传入的参数有效
        if not ViewButtonOfficEword:
            logging.warning("未提供文件名")
            return jsonify({
                'url': 'fileypess',
                'data': {},
                'type': '失败',
                'message': '未提供文件名',
                'Time': glode.NowTime(),
            }), 400  # 返回400状态码

        # 遍历文件类型
        for file_type in glode.fileypesss():
            if ViewButtonOfficEword.endswith(file_type):
                logging.info(f"成功匹配文件类型: {file_type}")
                return jsonify({
                    'url': 'fileypess',
                    'data': file_type,
                    'type': '成功',
                    'Time': glode.NowTime(),
                })

        logging.warning(f"未匹配到文件类型: {ViewButtonOfficEword}")
        return jsonify({
            'url': 'fileypess',
            'data': ViewButtonOfficEword,
            'type': '失败',
            'message': '未匹配到文件类型',
            'Time': glode.NowTime(),
        }), 404  # 返回404状态码

    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'url': 'fileypess',
            'data': {},
            'type': '失败',
            'message': str(e),
            'Time': glode.NowTime(),
        }), 500  # 返回500状态码
