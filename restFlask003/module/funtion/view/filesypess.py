# routes/filesypess_blueprint.py

from flask import Blueprint, request, jsonify
import os
from module.glode import glode
import logging

# 创建蓝图对象
filesypess_blueprint = Blueprint('filesypess_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@filesypess_blueprint.route('/filesypess', methods=['POST', 'GET'])
def filesypess():
    filesypessPath = request.args.get('filesypessPath')
    
    try:
        # 检查路径是否有效
        if not filesypessPath or not os.path.exists(filesypessPath):
            logging.warning(f"路径不存在: {filesypessPath}")
            return jsonify({
                'url': 'filesypess',
                'data': {},
                'type': '失败',
                'message': '路径不存在',
                'Time': glode.NowTime(),
            }), 404

        filesypessPathlist = os.listdir(filesypessPath)
        filesypessPathlistType = {}
        filesypessPathlistTypes = {}

        # 遍历文件列表
        for i, file_name in enumerate(filesypessPathlist):
            filesypessPathlistpath = os.path.join(filesypessPath, file_name)
            file_type_found = False

            # 检查文件扩展名
            for file_type in glode.fileypesss():
                if filesypessPathlistpath.endswith(file_type):
                    filesypessPathlistType[i] = file_type
                    filesypessPathlistTypes[i] = {'index': i, 'filesypessPathlistType': '查看文件'}
                    file_type_found = True
                    break
            
            # 如果没有找到匹配的类型
            if not file_type_found:
                filesypessPathlistType[i] = False

        return jsonify({
            'url': 'filesypess',
            'data': filesypessPathlistType,
            'filesypessPathlistTypes': filesypessPathlistTypes,
            'type': '成功',
            'test': filesypessPathlist,
            'Time': glode.NowTime(),
        })

    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'url': 'filesypess',
            'data': {},
            'type': '失败',
            'message'       
            'Time': glode.NowTime(),
        }), 500
