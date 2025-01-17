
from flask import Blueprint, request, send_file, jsonify
import os
import shutil

import logging
# 创建蓝图对象
login_blueprint = Blueprint('login_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

@login_blueprint.route('/login', methods=['GET'])
def login():
   
    MD5AESBehind = request.args.get('MD5AESBehind')
    timestamp = request.args.get('Time')
    
    
    return jsonify({
                'url': 'login',
                'data': MD5AESBehind,
                'Time': timestamp
            })

    # try:
    #     # 如果路径不是文件夹
    #     if not os.path.isdir(downloadPathName):
    #         print(downloadName, downloadPathName)
    #         if not os.path.exists(downloadPathName):
    #             logging.error(f"文件不存在: {downloadPathName}")
    #             return jsonify({
    #                 'error': '文件未找到',
    #                 'message': f'指定的文件不存在: {downloadPathName}'
    #             }), 404
    #         return send_file(downloadPathName, as_attachment=True)

    #     # 如果文件夹不为空
    #     elif os.listdir(downloadPathName):
    #         # 压缩文件夹
    #         zip_file_path = os.path.join(glode.asfliezip(), f'{downloadName}.zip')
    #         shutil.make_archive(zip_file_path[:-4], 'zip', downloadPathName)

    #         # 发送压缩文件
    #         download_response = send_file(zip_file_path, as_attachment=True)

    #         # 执行外部批处理文件（可选）
    #         os.system('./restFlask003/template/as/dropdowln.bat')

    #         return download_response

    #     # 如果文件夹为空
    #     else:
    #         return jsonify({
    #             'url': 'download',
    #             'data': '',
    #             'type': '文件夹为空',
    #             'Time': glode.NowTime()
    #         })

    # except shutil.Error as e:
    #     logging.error(f"压缩文件夹时发生错误: {e}")
    #     return jsonify({
    #         'error': '压缩错误',
    #         'message': str(e)
    #     }), 500

    # except Exception as e:
    #     logging.error(f"发生错误: {e}")
    #     return jsonify({
    #         'error': '内部服务器错误',
    #         'message': str(e)
    #     }), 500
