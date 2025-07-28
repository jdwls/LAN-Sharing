from flask import Blueprint, request, send_file, jsonify, make_response
import os
import shutil
from pathlib import Path
from flask_cors import CORS
import logging
import module.glode.glode as glode
import json
from threading import Lock
# 创建蓝图对象
after_chat_information_list_blueprint = Blueprint('after_chat_information_list_blueprint', __name__)
CORS(after_chat_information_list_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
file_lock = Lock()
@after_chat_information_list_blueprint.route('/after_chat_information_list', methods=['GET'])
def after_chat_information_list():
    sned_user_name=request.args.get('sned_user_name')
    receive_user_name=request.args.get('receive_user_name')
    print(sned_user_name, receive_user_name)
    try:
        if sned_user_name and receive_user_name:
            sort_data=[sned_user_name,receive_user_name]
            sort_data= sorted(sort_data)
            send_name_to_report_name_path='../restFlask003/template/char_list/'+sort_data[0]+'_to_'+sort_data[1]+'.json'
            if os.path.exists(send_name_to_report_name_path):
                with file_lock:
                    char_list_room=glode.read_char_list(send_name_to_report_name_path)
                    return jsonify({'code': 200, 'msg': '获取聊天记录成功', 'data': char_list_room})
            else:
                return jsonify({'code': 404, 'msg': '聊天记录不存在'})
        else:
            return jsonify({'code': 400, 'msg': '缺少必要参数'})
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)})