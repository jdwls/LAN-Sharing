from flask import Blueprint, request, jsonify
import logging
import json
import hmac
import module.glode.glode as glode
# 创建蓝图对象
login_blueprint = Blueprint('login_blueprint', __name__)
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', mode='a'),
        logging.StreamHandler()
    ]
)
# 常量定义
@login_blueprint.route('/login', methods=['GET'])
def login():
    username = request.args.get('name')
    password = request.args.get('MD5AESBehind')
    Time= request.args.get('Time')
    # 判断用户名、密码和时间是否为空
    try:
        if not username or not password or not Time:
            return jsonify({'status': 'error', 'message': '用户名或密码不能为空'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': '参数错误'}), 200
    # 读取管理员数据
    try:
        with open(glode.AdminPathJson(), 'r', encoding='utf-8') as f:
            AdminDataJson = json.load(f)
            f.close()
    except Exception as e:
        return jsonify({'status': 'error', 'message': '服务器错误'}), 200
    # 读取用户数据
    try:
        with open(glode.UresPathJson(), 'r', encoding='utf-8') as f:
            UserPathjson = json.load(f)
            f.close()
    except Exception as e:
        return jsonify({'status': 'error', 'message': '服务器错误'}), 200
    # 检查用户名和密码是否匹配
    try:
        for i in range(len(AdminDataJson)):
            if AdminDataJson[i]['name'] == username and AdminDataJson[i]['password'] == password:
                with open(glode.AdminPathJson(), 'w', encoding='utf-8') as f:
                    AdminDataJson[i]['Time'] = Time
                    json.dump(AdminDataJson, f, ensure_ascii=False, indent=4)
                    f.close()
                return jsonify({'status': 'success', 'message': '登录成功', 'data': username}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': '服务器错误'}), 200
    try:
        for i in range(len(UserPathjson)):
            if UserPathjson[i]['name'] == username and UserPathjson[i]['password'] == password:
                with open(glode.UresPathJson(), 'w', encoding='utf-8') as f:
                    UserPathjson[i]['Time'] = Time
                    json.dump(UserPathjson, f, ensure_ascii=False, indent=4)
                    f.close()
                return jsonify({'status': 'success', 'message': '登录成功', 'data': username}), 200
        return jsonify({'status': 'error', 'message': '用户名或密码错误'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': '服务器错误'}), 200
    