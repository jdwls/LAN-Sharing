from flask import Blueprint, request, send_file
import os
from ...glode import glode

# 创建蓝图对象
video_play_blueprint = Blueprint('video_play', __name__)


@video_play_blueprint.route('/VideoPlay', methods=['POST', 'GET'])
def VideoPlay():
    video_path = request.args.get('VideoPlay')
    Chart_Romm_video_path=str(glode.path()+video_path)
    print(Chart_Romm_video_path)
    is_video_file=0
    if video_path:
        is_video_file=1
    if is_video_file and os.path.isfile(video_path):
        if is_video_file_type(video_path)[0]:
            return send_file(video_path, mimetype=is_video_file_type(video_path)[1])
    if is_video_file and os.path.isfile(Chart_Romm_video_path):
        if is_video_file_type(Chart_Romm_video_path)[0]:
            return send_file(Chart_Romm_video_path, mimetype=is_video_file_type(Chart_Romm_video_path)[1])
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
def is_video_file_type(video_path):
    if video_path.endswith('.ts'):
        mime_type = 'video/mp2t'
        return [True,mime_type] 
    elif video_path.endswith('.mp4'):
        mime_type = 'video/mp4'
        return [True,mime_type] 
    else:
        return False

    
