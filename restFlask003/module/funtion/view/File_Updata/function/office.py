# routes/office_blueprint.py

from flask import Blueprint, request, send_file, jsonify
import os
import logging

# 创建蓝图对象
office_blueprint = Blueprint('office_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@office_blueprint.route('/office', methods=['POST', 'GET'])
def office():
    uploadpath = request.args.get('dw')

    # 检查上传路径是否存在
    if not uploadpath:
        logging.warning("未提供文件路径")
        return jsonify({
            'error': '未提供文件路径'
        }), 400  # 返回400状态码

    if not os.path.exists(uploadpath):
        logging.error(f"文件未找到: {uploadpath}")
        return jsonify({
            'error': '文件未找到'
        }), 404  # 返回404状态码

    try:
        # 发送文件
        return send_file(uploadpath)
    except Exception as e:
        logging.error(f"发送文件时发生错误: {e}")
        return jsonify({
            'error': '内部服务器错误',
            'message': str(e)
        }), 500  # 返回500状态码
