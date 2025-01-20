
from flask import Blueprint, request, send_file, jsonify,make_response
import os
import shutil
from pathlib import Path
import logging
# 创建蓝图对象
login_blueprint = Blueprint('login_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

@login_blueprint.route('/login', methods=['GET'])
def login():
    name=request.args.get('name')
    MD5AESBehind = request.args.get('MD5AESBehind')
    timestamp = request.args.get('Time')
    GuanLiQuanXianLuj='template/UseSql/Permission/'
    UseNamepath=Path(GuanLiQuanXianLuj+name+'.txt')
    Cookietime=60*60*24*1
    try:
        if UseNamepath.exists():
            with open(UseNamepath, 'r',encoding='utf-8') as file:
                password=file.read()
            if password==MD5AESBehind:
                response = make_response('cookie')
                response.set_cookie('  ', name, max_age=Cookietime)
                return jsonify({
                        'url': 'login',
                        'Time': timestamp,
                        'message':'密码正确',
                    })
                        
            else:
                return jsonify({
                        'url': 'login',
                        'Time': timestamp,
                        'message':'密码错误'
                    })
        else:
            return jsonify({
                        'url': 'login',
                        'Time': timestamp,
                        'message':'用户不存在'
                    })
    except Exception as e:
        logging.error(f"发生错误: {e}")
        return jsonify({
            'error': '内部服务器错误',
            'message': str(e)
        }), 500
    

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
