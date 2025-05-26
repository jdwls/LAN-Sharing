from flask import Blueprint, request, jsonify
import json
import logging
from pathlib import Path
import module.glode.glode as glode
# 创建蓝图对象
Logup_blueprint = Blueprint('Logup_blueprint', __name__)
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
# 常量定义
@Logup_blueprint.route('/Logup', methods=['GET'])
def Logup():
    """注册用户"""
    username = request.args.get('name')
    password = request.args.get('MD5AESBehind')
    reg_time = request.args.get('Time')
    # 判断用户名、密码和注册时间是否为空
    try:
        if not username or not password or not reg_time:
            return jsonify({'status': 'error', 'message': '用户名或密码不能为空'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': '参数错误'}), 400
    # 读取用户数据
    try:
        with open(glode.UresPathJson(), 'r', encoding='utf-8') as f:
            users = json.load(f)
            f.close()
    except Exception as e:
        return jsonify({'status': 'error', 'message': '服务器错误'}), 500
    # 检查用户名是否已存在
    try:
        for i in range(len(users)):
            if users[i]['name'] == username:
                return jsonify({'status': 'error', 'message': '用户名已存在'}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': '服务器错误'}), 500
    # 添加新用户
    try:
        # 添加新用户
        new_user = {
            'name': username,
            'password': password,
            '注册时间': reg_time,
            "Time": 0,
        }
        users.append(new_user)
        # 保存数据
        with open(glode.UresPathJson(), 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
            f.close()
        return jsonify({'status': 'success', 'message': '注册成功','data':username}), 200
    except IOError as e:
        return jsonify({'status': 'error', 'message': '服务器错误'}), 500
    