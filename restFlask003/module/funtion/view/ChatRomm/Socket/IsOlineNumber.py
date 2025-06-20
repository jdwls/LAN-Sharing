from flask import Blueprint, request, send_file, jsonify, make_response
from flask_cors import CORS
import logging
import module.glode.glode as glode
import json
from flask_socketio import SocketIO,send,emit
# 创建蓝图对象
IsOlineNumber_blueprint = Blueprint('IsOlineNumber_blueprint', __name__)
CORS(IsOlineNumber_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
@IsOlineNumber_blueprint.route('/IsOlineNumber', methods=['GET'])



        