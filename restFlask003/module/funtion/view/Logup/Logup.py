from flask import Blueprint, request, send_file, jsonify
import os
import shutil
import logging


# 创建蓝图对象
Logup_blueprint = Blueprint('Logup_blueprint', __name__)


# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


@Logup_blueprint.route('/Logup', methods=['GET'])
def Logup():
    MD5AESBehind = request.args.get('MD5AESBehind')
    name = request.args.get('name')
    GuanLiQuanXianLuj = 'template/UseSql/Permission/'
    UseNamepath = GuanLiQuanXianLuj + name + '.txt'
    try:
        if os.path.exists(GuanLiQuanXianLuj) and os.path.isdir(GuanLiQuanXianLuj):
            if os.path.exists(UseNamepath):
                logging.error(f"文件夹已经存在: {UseNamepath}")
                return jsonify({
                    'error': '用户名已经存在,请重新输入用户名',
                    'message': name
                }), 200
            else:
                with open(UseNamepath, 'w',encoding='utf-8') as file:
                    file.write(str(MD5AESBehind))
                logging.error(f"文件创建成功: {UseNamepath}")
                return jsonify({
                    'success': '用户已经注册成功',
                    'message': name
                }), 200
        else:
            logging.error(f"权限文件夹不存在或不是一个目录: {GuanLiQuanXianLuj}")
            return jsonify({
                'error': '权限文件夹不存在或不是一个目录',
                'message': GuanLiQuanXianLuj
            }), 500
    except Exception as e:
        logging.error(f"Error creating file: {e}")
        return jsonify({
            'error': '创建文件时发生错误',
            'message': str(e)
        }), 500