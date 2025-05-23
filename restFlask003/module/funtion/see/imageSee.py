# routes/image_see_blueprint.py

from flask import Blueprint, request
from flask import send_file
import os
from ...glode import glode
# 创建蓝图对象
imagesee_blueprint = Blueprint('image_see', __name__)


@imagesee_blueprint.route('/imageSee', methods=['POST', 'GET'])
def imageSee():
    image_see_name = request.args.get('imageSeeName')

    # 检查图像文件是否存在
    if not image_see_name or not os.path.isfile(image_see_name):
        return {
            'url': 'image_see',
            'data': {},
            'type': '失败',
            'message': '图像文件不存在',
            'Time': glode.NowTime(),  # 根据需要修改为当前时间
        }

    return send_file(image_see_name)
