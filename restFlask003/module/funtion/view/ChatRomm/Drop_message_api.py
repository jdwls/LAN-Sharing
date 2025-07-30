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
Drop_message_api_blueprint = Blueprint('Drop_message_api_blueprint', __name__)
CORS(Drop_message_api_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
file_lock = Lock()
@Drop_message_api_blueprint.route('/Drop_message_api', methods=['GET'])
def Drop_message_api():
    message_index=int(request.args.get('message_index'))
    sned_user_name=request.args.get('send_name')
    receive_user_name=request.args.get('report_name')
    try:
        if sned_user_name and receive_user_name :
            sort_data=[sned_user_name,receive_user_name]
            sort_data= sorted(sort_data)
            send_name_to_report_name_path=glode.path()+'template/char_list/'+sort_data[0]+'_to_'+sort_data[1]+'.json'
            if os.path.exists(send_name_to_report_name_path):
                with file_lock:
                    char_list_room=glode.read_char_list(send_name_to_report_name_path)
                if char_list_room[message_index]['revocation_or_drop']['drop']["drop_name"][0]==0:
                    char_list_room[message_index]['revocation_or_drop']['drop']["drop_name"][0]=sned_user_name
                    char_list_room[message_index]['revocation_or_drop']['drop']["drop_state"][0]=False
                else:
                    char_list_room[message_index]['revocation_or_drop']['drop']["drop_name"][1]=sned_user_name
                    char_list_room[message_index]['revocation_or_drop']['drop']["drop_state"][1]=False    
                with file_lock:
                       with open(send_name_to_report_name_path,'w',encoding='utf=8') as f:
                           json.dump(char_list_room, f, ensure_ascii=False, indent=4)
                           f.close()
                with file_lock:
                    char_list_room=glode.read_char_list(send_name_to_report_name_path) 
                return jsonify({
                    'code':200,
                    'msg':'成功',
                    'data':char_list_room
                })
            else:
                return jsonify({
                'code':404,
                'msg':'无聊天记录'
                })
        else:
            return jsonify({
                'code':400,
                'msg':'参数错误'
                })
    except Exception as e:
        return jsonify({'code': 500, 'msg': str(e)})
    # with open(glode.)