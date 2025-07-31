
from flask import Blueprint, request, send_file, jsonify, make_response
import os
import shutil
from pathlib import Path
from flask_cors import CORS
import logging
# 创建蓝图对象
Cookie_blueprint = Blueprint('Cookie_blueprint', __name__)
CORS(Cookie_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


@Cookie_blueprint.route('/Cookie', methods=['GET'])
def Cookie():
    name = request.args.get('name')
    Cookietime = 60*60*24*1
    try:
        if name == '':
            response = make_response('cookie')
            response.set_cookie('usename', 'Youke',
                                max_age=Cookietime, secure=True)
            return response
        else:
            response = make_response('cookie')
            response.set_cookie(
                'usename', name, max_age=Cookietime, secure=True, samesite='None',)
            return response
    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'error': '内部服务器错误',
            'message': str(e)
        }), 500
