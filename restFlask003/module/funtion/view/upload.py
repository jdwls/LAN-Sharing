from flask import Blueprint, render_template, request, jsonify
import os
import logging
from module.glode import glode
from module.funtion.common import readdirpath

# 创建蓝图对象
upload_bp = Blueprint('upload', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 路由：渲染上传页面
# 路由：处理文件上传


@upload_bp.route('/uploader', methods=['POST'])
def uploader():
    # 读取上传目录
    try:
        with open(glode.dirpath(), encoding="utf-8") as f:
            upload_dir = f.read().strip()
    except Exception as e:
        logging.error(f"无法读取上传目录: {str(e)}")
        return jsonify({'error': '无法读取上传目录'}), 500

    # 检查请求中是否有文件
    if 'file' not in request.files:
        logging.warning("未找到文件部分")
        return jsonify({'error': '没有文件部分'}), 400

    file = request.files['file']
    if file.filename == '':
        logging.warning("未选择文件")
        return jsonify({'error': '未选择文件'}), 400

    # 确保路径安全，防止目录遍历攻击
    upload_path = os.path.join(readdirpath.dirMOde(
        glode.dirpath()), upload_dir, file.filename)
    upload_path = os.path.abspath(upload_path)  # 获取绝对路径
    base_dir = os.path.abspath(readdirpath.dirMOde(glode.dirpath()))

    if not upload_path.startswith(base_dir):
        logging.warning("试图上传到非法路径: %s", upload_path)
        return jsonify({'error': '无效的上传路径'}), 400

    # 确保上传目录存在
    os.makedirs(os.path.dirname(upload_path), exist_ok=True)

    try:
        file.save(upload_path)
        log_upload(file.filename, upload_dir)
        return jsonify({
            'url': 'uploader',
            'type': '文件',
            'iss': '文件上传成功'
        }), 200
    except Exception as e:
        logging.error(f"文件上传失败: {str(e)}")
        return jsonify({'error': str(e)}), 500


def log_upload(filename, upload_dir):
    """记录文件上传信息到日志"""
    try:
        with open(glode.dirPathLog(), 'a', encoding="utf-8") as log_file:
            log_file.write(glode.NowTime())
            log_file.write('        ')
            log_file.write(f'保存文件：{filename}      ')
            log_file.write(f'保存路径：{upload_dir}')
            log_file.write('\n')
        logging.info(f"文件 {filename} 成功上传到 {upload_dir}")
    except Exception as e:
        logging.error(f"记录日志失败: {str(e)}")
