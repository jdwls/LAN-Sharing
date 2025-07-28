from flask import Blueprint, request, jsonify
import logging
import json
import os
from threading import Lock
from collections import defaultdict
from flask_socketio import SocketIO, emit, disconnect
import module.glode.glode as glode
from datetime import datetime
import threading
IsOlineNumber_blueprint = Blueprint('IsOlineNumber_blueprint', __name__)
socketio = SocketIO()

# 使用内存存储在线状态和聊天记录
# online_users = defaultdict(int)  # 格式: {username: 连接计数}
# active_sessions = {}  # 格式: {session_id: username}
# chat_messages = defaultdict(list)  # 格式: {chat_id: [messages]}
file_lock = Lock()

# 初始化在线用户文件
ONLINE_FILE = glode.IsOlineNumbers()
with file_lock:
        with open(ONLINE_FILE, 'w') as f:
            json.dump({"online_users": []}, f)

# def get_chat_id(user1, user2):
#     """生成标准化的聊天ID"""
#     return '_'.join(sorted([user1, user2]))

# # Socket事件处理
@socketio.on('connect')
def handle_connect():
    session_id = request.sid
    logging.info(f'客户端连接: {session_id}')
@socketio.on('user_login_chat_room')
def socket_user_login_chat_room(data):
    with file_lock:
        with open(ONLINE_FILE, 'r', encoding='utf-8') as f:
            online_data = json.load(f)
            f.close()
    username = {'user_name':data.get('username'), 'session_id': request.sid}
    is_new_user=True
    for i in range(len(online_data['online_users'])):
        if  online_data['online_users'][i]['user_name']==data.get('username'):
            online_data['online_users'][i]['session_id'] = request.sid
            is_new_user =False
    with file_lock:
        with open(ONLINE_FILE,'w',encoding='utf-8') as f:
            json.dump(online_data,f)
            f.close()
        with open(ONLINE_FILE,'r',encoding='utf-8') as f:
            online_data = json.load(f)
            f.close()
    if is_new_user:
        online_data['online_users'].append(username)
        with file_lock:
            with open(ONLINE_FILE, 'w', encoding='utf-8') as f:
                json.dump(online_data, f)
                f.close()
        # print('新用户登录:', username)
    emit('updata_online_urse_list', online_data, broadcast=True)
    disconnect_user_list_fun()
@socketio.on('disconnect')
def handle_disconnect():
    disconnect_user_reduce_list_fun(request.sid)
    disconnect_user_list_fun()
def disconnect_user_reduce_list_fun(session_id):
    session_id_szu=[]
    with file_lock:
        with open(ONLINE_FILE, 'r', encoding='utf-8') as f:
            online_data = json.load(f)
            f.close()
    for i in range(len(online_data['online_users'])):
        if online_data['online_users'][i]['session_id']==session_id:
             session_id_szu.append(i)
    for i in range(len(session_id_szu)):
        online_data['online_users'].pop(session_id_szu[i])
    with file_lock:        
        with open(ONLINE_FILE, 'w', encoding='utf-8') as f:
            json.dump(online_data, f)
            f.close()
    emit('updata_online_urse_list', online_data, broadcast=True)
    logging.info(f'客户端断开连接: {session_id}')
    
def disconnect_user_list_fun():
    usrse_list_json=[]
    with file_lock:
        with open(glode.AdminPathJson(),'r',encoding='utf-8') as f:
            Ar_Admin_List_json=json.load(f)
            f.close()
        for i in range(len(Ar_Admin_List_json)):
            usrse_list_json.append(Ar_Admin_List_json[i].get('name'))
    with file_lock:
        with open(glode.UresPathJson(),'r',encoding='utf-8') as f:
            Ar_usrse_list_json=json.load(f)
            f.close()
        # with open(glode.AdminPathJson(),'r',encoding='utf-8') as f:
        for i in range(len(Ar_usrse_list_json)):
            usrse_list_json.append(Ar_usrse_list_json[i].get('name'))
    emit('disconnect_user_lists',usrse_list_json,broadcast=True)
@socketio.on('seend_message_data')
def handle_seend_message_data(data):
    sort_data=[data.get('send_name'),data.get('report_name')]
    sort_data= sorted(sort_data)
    send_name_to_report_name_path='../restFlask003/template/char_list/'+sort_data[0]+'_to_'+sort_data[1]+'.json'
    report_name_session_id=0
    mssage={'message':data.get('message'),
            'send_name':data.get('send_name'),
            'report_name':data.get('report_name'),
            'Time':data.get('Time'),
            'read_state':data.get('read_state'),
            'current_usrs':data.get('current_usrs')}
    if os.path.exists(send_name_to_report_name_path):
        with file_lock:
          char_list_room=glode.read_char_list(send_name_to_report_name_path)
          glode.write_char_list(char_list_room,mssage,send_name_to_report_name_path)
    if not os.path.exists(send_name_to_report_name_path):
        with file_lock:
            glode.write_char_list([],mssage,send_name_to_report_name_path)
    with file_lock:
        with open(ONLINE_FILE,'r',encoding='utf-8') as f:
            is_online_number_json=json.load(f)
            f.close()
    for i in range(len(is_online_number_json['online_users'])):
        if is_online_number_json['online_users'][i]['user_name']==data.get('report_name'):
            report_name_session_id=is_online_number_json['online_users'][i]['session_id']
            break
    # print(report_name_session_id)
    if(not report_name_session_id==0):
        emit('after_seend_message_data',mssage,to=report_name_session_id)
    emit('after_seend_message_data',mssage,to=request.sid)
