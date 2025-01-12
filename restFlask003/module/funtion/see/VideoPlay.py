from flask import Blueprint, request, send_file
import os
from ...glode import glode

# 创建蓝图对象
video_play_blueprint = Blueprint('video_play', __name__)

@video_play_blueprint.route('/VideoPlay', methods=['POST', 'GET'])
def VideoPlay():
    video_path = request.args.get('VideoPlay')

    # 检查视频文件是否存在
    if not video_path or not os.path.isfile(video_path):
        print("视频文件不存在")
        return {
            'url': 'VideoPlay',
            'data': {},
            'type': '失败',
            'message': '视频文件不存在',
            'Time': glode.NowTime(),  # 根据需要修改为当前时间
        }
    
    # 根据文件扩展名设置 MIME 类型
    if video_path.endswith('.ts'):
        mime_type = 'video/mp2t'
    elif video_path.endswith('.mp4'):
        mime_type = 'video/mp4'
    else:
        return {
            'url': 'VideoPlay',
            'data': {},
            'type': '失败',
            'message': '不支持的文件格式',
            'Time': glode.NowTime(),
        }

    return send_file(video_path, mimetype=mime_type)
