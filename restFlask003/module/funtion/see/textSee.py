# routes/text_see_blueprint.py

from flask import Blueprint, request
from flask import send_file
import os
from ...glode import glode

# 创建蓝图对象
textsee_blueprint = Blueprint('textsee_blueprint', __name__)

@textsee_blueprint.route('/textSee', methods=['POST', 'GET'])
def textSee():
    text_see_name = request.args.get('textSee')
    
    # 检查文本文件是否存在
    if not text_see_name or not os.path.isfile(text_see_name):
        return {
            'url': 'text_see',
            'data': {},
            'type': '失败',
            'message': '文本文件不存在',
            'Time': glode.NowTime(),  # 根据需要修改为当前时间
        }

    return send_file(text_see_name)
