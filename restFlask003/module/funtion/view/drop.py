# routes/file_blueprint.py

from flask import Blueprint, request, jsonify
import os
import shutil
from module.glode import glode
import logging

# 创建蓝图对象
drop_blueprint = Blueprint('drop_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@drop_blueprint.route('/dropFiles', methods=['GET'])
def dropFiles():
    dirse = request.args.get('dropFilesName')

    try:
        # 检查是否为目录并删除
        if os.path.isdir(dirse):
            shutil.rmtree(dirse)
            logging.info(f"成功删除文件夹: {dirse}")
            return jsonify({
                'url': 'dropFiles',
                'data': dirse,
                'type': '删除文件夹成功',
                'Time': glode.NowTime()
            })

        # 否则删除文件
        elif os.path.isfile(dirse):
            os.remove(dirse)
            logging.info(f"成功删除文件: {dirse}")
            return jsonify({
                'url': 'dropFiles',
                'data': dirse,
                'type': '删除文件成功',
                'Time': glode.NowTime()
            })

        # 如果不是文件也不是文件夹
        else:
            logging.error(f"删除失败: 文件或文件夹不存在: {dirse}")
            return jsonify({
                'error': '文件或文件夹未找到',
                'message': f'指定的文件或文件夹不存在: {dirse}'
            }), 404

    except PermissionError:
        logging.error(f"权限被拒绝: {dirse}")
        return jsonify({
            'error': '权限被拒绝',
            'message': f'您没有权限删除: {dirse}'
        }), 403

    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'error': '内部服务器错误',
            'message': str(e)
        }), 500
