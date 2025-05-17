# routes/file_blueprint.py

from flask import Blueprint, request, send_file, jsonify
import os
import shutil
import uuid
import logging
from werkzeug.utils import secure_filename
from module.glode import glode

download_blueprint = Blueprint('download_blueprint', __name__)

# 配置日志（确保仅配置一次）
if not logging.getLogger().handlers:
    logging.basicConfig(
        level=logging.INFO,
        filename=os.path.abspath('app.log'),
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


@download_blueprint.route('/download', methods=['GET'])
def download():
    downloadName = request.args.get('downloadName')
    downloadPathName = request.args.get('downloadPathName')

    # 检查参数是否存在
    if not downloadName or not downloadPathName:
        logging.error("缺少必要参数")
        return jsonify({
            'error': '参数缺失',
            'message': '必须提供downloadName和downloadPathName参数'
        }), 400

    # 安全处理文件名
    safe_download_name = secure_filename(downloadName)
    if not safe_download_name:
        return jsonify({
            'error': '无效文件名',
            'message': '提供的文件名无效'
        }), 400

    # 检查路径合法性

    try:
        # 处理文件下载
        if not os.path.isdir(downloadPathName):
            if not os.path.exists(downloadPathName):
                logging.error(f"文件不存在: {downloadPathName}")
                return jsonify({
                    'error': '文件未找到',
                    'message': f'指定的文件不存在: {downloadPathName}'
                }), 404
            return send_file(downloadPathName, as_attachment=True, download_name=safe_download_name)

        # 处理文件夹下载
        elif os.listdir(downloadPathName):
            # 生成唯一压缩文件名
            zip_filename = f"{safe_download_name}.zip"
            zip_file_path = os.path.join(glode.asfliezip(), zip_filename)
            # 创建压缩包
            shutil.make_archive(os.path.splitext(zip_file_path)[
                                0], 'zip', downloadPathName)
            # 发送文件并设置清理回调
            download_response = send_file(
                zip_file_path, as_attachment=True, download_name=zip_filename)

            @download_response.call_on_close
            def cleanup():
                try:
                    os.remove(zip_file_path)
                    logging.info(f"临时文件已删除: {zip_file_path}")
                except Exception as e:
                    logging.error(f"删除临时文件失败: {e}")

            return download_response

        else:
            return jsonify({
                'error': '空文件夹',
                'message': '指定的文件夹为空，无法下载'
            }), 400

    except shutil.Error as e:
        logging.error(f"压缩错误: {e}")
        return jsonify({
            'error': '压缩失败',
            'message': str(e)
        }), 500

    except Exception as e:
        logging.error(f"服务器错误: {e}")
        return jsonify({
            'error': '内部错误',
            'message': '服务器处理请求时发生错误'
        }), 500
