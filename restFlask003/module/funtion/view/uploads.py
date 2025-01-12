from flask import Blueprint, request, jsonify
import os
import logging
from module.glode import glode
from module.funtion.common import readdirpath, convert_size

# 创建蓝图对象
upload_bps = Blueprint('uploads', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@upload_bps.route('/uploaders', methods=['POST', 'GET'])
def uploaders():
    # 检查是否有文件上传
    if 'file' not in request.files:
        logging.warning("没有上传文件")
        return jsonify({
            "url": '/uploaders',
            "data": None,
            "type": '上传目录',
            "Time": glode.NowTime(),
            'iss': '没有上传文件'
        }), 400

    files = request.files['file']

    # 检查文件名是否为空
    if files.filename == '':
        log_upload_issue("没有选择文件")
        return jsonify({
            "url": '/uploaders',
            "data": None,
            "type": '上传目录',
            "Time": glode.NowTime(),
            'iss': '没有选择文件'
        }), 400

    # 获取文件的保存路径
    path = os.path.join(readdirpath.dirMOde(glode.dirpath()), files.filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)  # 创建目录

    try:
        files.save(path)  # 保存文件
        log_upload_success(files.filename, path)

        return jsonify({
            "url": '/uploaders',
            "data": files.filename,
            "type": '上传目录',
            "Time": glode.NowTime(),
            'iss': '目录上传成功',
            "Filesize": str(convert_size.convert_size(request.content_length))
        }), 200

    except Exception as e:
        logging.error(f"文件上传失败: {str(e)}")
        return jsonify({'error': '文件上传失败', 'message': str(e)}), 500

def log_upload_issue(message):
    """记录上传问题到日志"""
    with open(glode.dirPathLog(), 'a', encoding="utf-8") as f:
        f.write(glode.NowTime())
        f.write('        ')
        f.write(message + '\n')
    logging.warning(message)

def log_upload_success(filename, path):
    """记录成功上传文件的日志"""
    with open(glode.dirPathLog(), 'a', encoding="utf-8") as f:
        f.write(glode.NowTime())
        f.write('        ')
        f.write(f'{path}     目录上传成功\n')
    logging.info(f"文件 {filename} 成功上传到 {path}")
