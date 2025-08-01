from flask import Blueprint, request, send_file, jsonify, make_response
import os
import shutil
from pathlib import Path
from flask_cors import CORS
import logging
import module.glode.glode as glode
import json
from threading import Lock
# 创建蓝图对象
Chat_Room_File_Updata_api_blueprint = Blueprint('Chat_Room_File_Updata_api_blueprint', __name__)
CORS(Chat_Room_File_Updata_api_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
file_lock = Lock()
@Chat_Room_File_Updata_api_blueprint.route('/Chat_Room_File_Updata_api', methods=['GET','POST'])
def Chat_Room_File_Updata_api():
    formData= request.files['FileInput']
    file_name= request.form.get('file_name')
    file_type= request.form.get('file_type')
    send_name= request.form.get('send_name')
    report_name= request.form.get('report_name')
    sort_data=[send_name,report_name]
    try:
        if file_name:
            sort_data= sorted(sort_data)
            send_name_to_report_name_path = os.path.join(glode.path(),'template/char_list',f"{sort_data[0]}_to_{sort_data[1]}")
            send_name_to_report_name_File_path = os.path.join(send_name_to_report_name_path,file_name)
            os.makedirs(os.path.dirname(send_name_to_report_name_File_path), exist_ok=True)
            formData.save(send_name_to_report_name_File_path)
            return jsonify({'ms': '文件上传成功',
                            'data':{
                                'file_name': file_name,
                                'file_type': file_type,
                            },
                            }), 200
        return jsonify({'error': '文件上传失败'}), 200 
    except Exception as e:
        logging.error(f"文件上传失败: {str(e)}")
        return jsonify({'error': '文件上传失败'}), 500 
