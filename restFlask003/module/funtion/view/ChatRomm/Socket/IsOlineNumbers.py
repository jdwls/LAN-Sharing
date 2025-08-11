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
IsOlineNumbers_blueprint = Blueprint('IsOlineNumbers_blueprint', __name__)
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
    send_name_to_report_name_path= glode.path()+'template/char_list/'+sort_data[0]+'_to_'+sort_data[1]+'.json'
    print(send_name_to_report_name_path)
    report_name_session_id=0
    mssage={
            'message_index':data.get('message_index'),
            'message':data.get('message'),
            'message_type':data.get('message_type'),
            'send_name':data.get('send_name'),
            'report_name':data.get('report_name'),
            'Time':data.get('Time'),
            'read_state':data.get('read_state'),
            'revocation_or_drop':data.get('revocation_or_drop')
            }
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
    else:
        emit('after_seend_message_data',mssage,to=request.sid)
@socketio.on('revocation_message_socket')
def handle_revocation_message_socket(data):
    message_index=int(data.get('message_index'))
    sned_user_name=data.get('send_name')
    receive_user_name=data.get('report_name')
    report_name_session_id=0
    try:
        if sned_user_name and receive_user_name:
            sort_data=[sned_user_name,receive_user_name]
            sort_data= sorted(sort_data)
            send_name_to_report_name_path=glode.path()+'template/char_list/'+sort_data[0]+'_to_'+sort_data[1]+'.json'
            if os.path.exists(send_name_to_report_name_path):
                with file_lock:
                    char_list_room=glode.read_char_list(send_name_to_report_name_path)
                char_list_room[message_index]['revocation_or_drop']['revocation']["revocation_name"]=sned_user_name
                char_list_room[message_index]['revocation_or_drop']['revocation']["revocation_state"]=False  
                with file_lock:
                       with open(send_name_to_report_name_path,'w',encoding='utf=8') as f:
                           json.dump(char_list_room, f, ensure_ascii=False, indent=4)
                           f.close()
                with file_lock:
                    char_list_room=glode.read_char_list(send_name_to_report_name_path)
                with file_lock:
                    with open(ONLINE_FILE,'r',encoding='utf-8') as f:
                        is_online_number_json=json.load(f)
                        f.close()
                
                for i in range(len(is_online_number_json['online_users'])):
                    if is_online_number_json['online_users'][i]['user_name']==receive_user_name:
                        report_name_session_id=is_online_number_json['online_users'][i]['session_id']
                        break
                if not report_name_session_id==0:
                    emit('after_revocation_message_socket', char_list_room, to=report_name_session_id)
                    emit('after_revocation_message_socket', char_list_room, to=request.sid)     
                return 0 
            
    except Exception as e:
        emit('after_revocation_message_err_socket', char_list_room, to=request.sid)     
        return e
@socketio.on('seend_message_Files_socket')
def handle_seend_message_Files_socket(data):
    sort_data=[data.get('send_name'),data.get('report_name')]
    sort_data=sorted(sort_data)
    sort_data= sorted(sort_data)
    send_name_to_report_name_path= os.path.join(glode.path()+'template/char_list/'+sort_data[0]+'_to_'+sort_data[1]+'.json')
    try:
        with file_lock:
            with open(send_name_to_report_name_path,'r',encoding='utf-8') as f:
                char_list_room=json.load(f)
        
        
        emit('after_message_Files_socket',char_list_room, broadcast=True)
    except Exception as e:
        emit('after_message_Files_err_socket', {'error': str(e)}, to=request.sid)
        return jsonify({'error': '文件发送失败'}), 500  
    # with open(glode.)