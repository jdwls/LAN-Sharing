from flask import Blueprint, request,jsonify
import logging
import json
import os
from threading import Lock
from collections import defaultdict
from flask_socketio import SocketIO, emit, disconnect
import module.glode.glode as glode
IsOlineNumber_blueprint = Blueprint('IsOlineNumber_blueprint', __name__)
socketio = SocketIO()

# 使用内存存储在线状态
online_users = defaultdict(int)  # 格式: {username: 连接计数}
active_sessions = {}  # 格式: {session_id: username}
file_lock = Lock()

# 初始化在线用户文件
ONLINE_FILE = glode.IsOlineNumbers()
if not os.path.exists(ONLINE_FILE):
    with open(ONLINE_FILE, 'w') as f:
        json.dump({"online_users": []}, f)

def update_online_file():
    """更新在线用户文件"""
    with file_lock:
        online_list = list(online_users.keys())
        with open(ONLINE_FILE, 'w') as f:
            json.dump({"online_users": online_list}, f)

# Socket事件处理
@socketio.on('connect')
def handle_connect():
    session_id = request.sid
    logging.info(f'客户端连接: {session_id}')
    # 发送当前在线用户列表
    emit('current_online_users', {'online_users': list(online_users.keys())})

@socketio.on('disconnect')
def handle_disconnect():
    session_id = request.sid
    logging.info(f'客户端断开连接: {session_id}')
    if session_id in active_sessions:
        username = active_sessions[session_id]
        online_users[username] -= 1
        if online_users[username] <= 0:
            del online_users[username]
            update_online_file()
            # 广播更新
            emit('online_users_update', 
                 {'action': 'logout', 'username': username},
                 broadcast=True)
        
        del active_sessions[session_id]

@socketio.on('user_login')
def handle_user_login(data):
    session_id = request.sid
    username = data.get('username')
    if not username:
        logging.warning("登录请求缺少用户名")
        return
    
    active_sessions[session_id] = username
    is_new_user = username not in online_users
    
    online_users[username] += 1
    
    if is_new_user:
        update_online_file()
        # 广播新用户上线
        emit('online_users_update', 
             {'action': 'login', 'username': username},
             broadcast=True)
    
    # 返回当前在线用户列表
    emit('current_online_users', {'online_users': list(online_users.keys())})
@IsOlineNumber_blueprint.route('/IsOlineNumber', methods=['GET'])
def IsOlineNumber():
    urse_Name= request.args.get('urse_Name')
    print(urse_Name,'---------------------------------------------')
    try:
        if(urse_Name):
            with open(glode.IsOlineNumbers(), 'r', encoding='utf-8') as f:
                IsOlineNumber_json = json.load(f)
                f.close(),  
            IsOlineNumber_json['online_users'].remove(urse_Name)
            with open(glode.IsOlineNumbers(), 'w', encoding='utf-8') as f:
                json.dump(IsOlineNumber_json, f)
                f.close()
            return jsonify({
                'code':200,
                'meg':'退出成功',
                'data':IsOlineNumber_json,
            })
        return jsonify({
            'code':200,
            'meg':'网络问题'
        })
    except Exception as e:
        return jsonify({
            'code':500,
            'meg':e
        })
@socketio.on('chat_message')
def chat_message(res):
    path = 'restFlask003/template/char_list'
    # 确保目录存在
    if not os.path.exists(path):
        os.makedirs(path)
    
    # 提取并标准化用户名（按字母顺序排序）
    user1, user2 = sorted ([res['send_name'], res['report_name']])
    # 生成唯一文件名（按固定顺序）
    expected_filename = str(user1)+'_to_'+str(user2)+'.json'
    char_list_path = path+ '/' + expected_filename
    # 直接使用标准化路径（无论文件是否存在）
    # 后续在此路径读写聊天记录即可
    # 示例：追加新消息到文件 
    is_file_exists = os.path.exists(char_list_path)
    if not is_file_exists:
        with open(char_list_path, 'w', encoding='utf-8') as f:
            f.write('[]')
            f.close()
    char_list_infomation=glode.read_char_list(char_list_path)
    is_char_list_infomation_state=glode.write_char_list(json.loads(char_list_infomation),res,char_list_path)
    if is_char_list_infomation_state:
        emit(res['report_name'], res,broadcast=True, include_self=True)
        emit(res['send_name'], res,broadcast=True, include_self=True)