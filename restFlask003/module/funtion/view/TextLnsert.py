# routes/dir_blueprint.py

from flask import Blueprint, jsonify, request
import os
from module.glode import glode
from module.funtion.common import readdirpath
import logging

# 创建蓝图对象
TextLnsert_blueprint = Blueprint('TextLnsert_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@TextLnsert_blueprint.route('/TextLnsert', methods=['POST', 'GET'])
def TextLnsert():

    TextConter = request.args.get('TextConter')
    NowPath = request.args.get('NowPath')
    TextName = request.args.get('TextName')+'.txt'
    try:
        if os.path.exists(NowPath+"/"+TextName) == True:
            return jsonify({
                "error": "当前存在相关文件",
                'message': '创建文本文件失败',
                "Time": glode.NowTime(),
                "url": 'TextLnsert',
                'data': TextName
            }), 202
        # 获取所有文件夹
        else:
            with open(NowPath + "/" + TextName, 'w+', encoding="utf-8") as TextNameFiles:
                if TextConter != '':
                    TextNameFiles.write(TextConter)

            return jsonify({
                'message': '创建文本文件成功',
                "Time": glode.NowTime(),
                "url": 'TextLnsert',
                'data': TextName
            }), 202

    except Exception as e:
        logging.error(f"发生错误: {e}")
        # 返回500状态码
        return jsonify({'error': '内部服务器错误', 'message': str(e)}), 500
