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
socketio = SocketIO()
@socketio.on('socketio_ures')
def socketio_ures(data):
    print(data)
@socketio.on('connect')
def handle_connect():
    print("Client connected ----------------------------------------------------------------------------------------------------")
    # 发送欢迎消息给新连接的客户端
@IsOlineNumber_blueprint.route('/IsOlineNumber', methods=['GET'])
def IsOlineNumber():
    print("IsOlineNumber")