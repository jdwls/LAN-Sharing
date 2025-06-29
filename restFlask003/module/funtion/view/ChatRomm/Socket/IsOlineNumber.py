from flask import Blueprint, request
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