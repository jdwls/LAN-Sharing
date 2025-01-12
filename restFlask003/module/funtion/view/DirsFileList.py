from flask import Blueprint, request, jsonify
import os
from module.glode import glode
from module.funtion.common import readdirpath
import logging

# 创建蓝图对象
DirsFileList_blueprint = Blueprint('DirsFileList_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@DirsFileList_blueprint.route('/DirsFileList', methods=['POST', 'GET'])
def DirsFileList():
    # 获取请求参数中的目录路径
   
    try:
        # 根据参数决定目录路径
        
        directory_path = readdirpath.dirMOde(glode.dirpath())
        logging.info(f"使用用户提供的目录路径: {directory_path}")

        # 检查目录是否存在
        if not os.path.exists(directory_path):
            logging.error(f"目录不存在: {directory_path}")
            return jsonify({
                'error': '目录未找到',
                'message': f'指定的目录不存在: {directory_path}'
            }), 404

        # 列出目录下的文件和文件夹
        files_and_dirs = os.listdir(directory_path)

        # 日志记录成功
        logging.info(f"成功列出目录: {directory_path}, 文件和文件夹: {files_and_dirs}")
        
        return jsonify({
            'url': 'DirsFileList',
            'data': files_and_dirs,
            'type': '当前目录下的所有文件和文件夹',
            'Time': glode.NowTime()
        })
    
    except PermissionError:
        logging.error(f"权限被拒绝: {directory_path}")
        return jsonify({
            'error': '权限被拒绝',
            'message': f'您没有权限访问: {directory_path}'
        }), 403
    
    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'error': '内部服务器错误',
            'message': str(e)
        }), 500
