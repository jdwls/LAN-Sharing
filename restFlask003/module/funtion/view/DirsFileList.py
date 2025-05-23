from flask import Blueprint, request, jsonify   
import os
from module.glode import glode
from module.funtion.common import readdirpath
import logging
import filetype

# 创建蓝图对象
DirsFileList_blueprint = Blueprint('DirsFileList_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(levelname)s - %(message)s')

@DirsFileList_blueprint.route('/DirsFileList', methods=['POST', 'GET'])
def DirsFileList():
    # 获取请求参数
    dir_path = request.args.get('DirsFileList', '')  # 默认为空字符串
    logging.info(f"请求路径参数: {dir_path}")

    try:
        # 确定目标目录路径
        directory_path = readdirpath.dirMOde(glode.dirpath()) if not dir_path else dir_path
        
        # 检查目录是否存在
        if not os.path.exists(directory_path):
            logging.error(f"目录不存在: {directory_path}")
            return jsonify({
                'error': '目录未找到',
                'message': f'指定的目录不存在: {directory_path}'
            }), 404

        # 获取目录内容
        items = os.listdir(directory_path)
        result = {}

        for index, item_name in enumerate(items):
            item_path = os.path.join(directory_path, item_name)
            result[index] = {
                'index': index,
                'data': item_name,
                'type': None,
            }
            # 判断是目录还是文件
            if os.path.isdir(item_path):
                result[index]['type'] = '打开目录'
            else:
                # 文件类型检测
                kind = filetype.guess(item_path)
                for m in glode.fileypesss2():
                    if kind:
                        if kind.mime.startswith(m[list(m.keys())[0]])==True:
                            print(kind.mime.startswith(m[list(m.keys())[0]]),item_name)
                            result[index]['type'] = '查看文件'
                            break
                
        return jsonify({
            'success': True,
            'path': directory_path,
            'items': result,
            'timestamp': glode.NowTime()
        })

    except PermissionError:
        logging.error(f"权限不足: {directory_path}")
        return jsonify({
            'error': '权限不足',
            'message': f'没有权限访问: {directory_path}'
        }), 403
    except Exception as e:
        logging.error(f"服务器错误: {str(e)}")
        return jsonify({
            'error': '服务器错误',
            'message': str(e)
        }), 500