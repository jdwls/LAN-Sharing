from flask import Blueprint, request, jsonify
import logging
import json
import hmac
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
ADMIN_PATH = 'restFlask003/template/uresAndAdmin/Admin.json'
USER_PATH = 'restFlask003/template/uresAndAdmin/ures.json'
def load_json_data(file_path):
    """加载JSON文件数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"文件不存在: {file_path}")
        return None
    except json.JSONDecodeError:
        logging.error(f"JSON解析错误: {file_path}")
        return None
    except Exception as e:
        logging.error(f"读取文件异常: {file_path} - {str(e)}")
        return None
def save_json_data(file_path, data):
    """保存数据到JSON文件"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        logging.error(f"保存文件失败: {file_path} - {str(e)}")
        return False
def validate_credentials(data, username, password_hash):
    """验证用户凭证"""
    for user in data:
        if user['name'] == username:
            # 使用安全比较防止时序攻击
            if hmac.compare_digest(user['password'], password_hash):
                return user
            return None  # 密码错误但用户存在
    return None  # 用户不存在
@login_blueprint.route('/login', methods=['GET'])
def login():
    # 参数校验
    required_params = ('name', 'MD5AESBehind', 'Time')
    if not all(request.args.get(param) for param in required_params):
        logging.warning("缺少必要参数")
        return jsonify({"code": 400, "msg": "参数缺失"}), 400

    username = request.args['name']
    password_hash = request.args['MD5AESBehind']
    timestamp = request.args['Time']
    # 先验证管理员账户
    admin_data = load_json_data(ADMIN_PATH)
    if admin_data is not None:
        admin = validate_credentials(admin_data, username, password_hash)
        if admin:
            admin['Time'] = timestamp
            if save_json_data(ADMIN_PATH, admin_data):
                return jsonify({"code": 200, "msg": "登录成功",'Quthority':"管理员"})
            return jsonify({"code": 500, "msg": "服务器错误"}), 500

    # 验证普通用户
    user_data = load_json_data(USER_PATH)
    if user_data is not None:
        user = validate_credentials(user_data, username, password_hash)
        if user:
            user['Time'] = timestamp
            if save_json_data(USER_PATH, user_data):
                return jsonify({"code": 200, "msg": "登录成功",'Quthority':"普通用户"})
            return jsonify({"code": 500, "msg": "服务器错误"}), 500
        # 检查是否存在用户但密码错误
        if any(u['name'] == username for u in user_data):
            return jsonify({"code": 400, "msg": "登录失败"}), 400
    logging.warning(f"用户不存在: {username}")