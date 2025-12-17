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
    chatRoomimages=glode.path()+image_see_name
    Is_Image_File=0
    # 检查图像文件是否存在
    if image_see_name:
        Is_Image_File=1
    if os.path.isfile(image_see_name):
        Is_Image_File=11
    if os.path.isfile(chatRoomimages):
        Is_Image_File=111
    if Is_Image_File==11:
        return send_file(image_see_name)
    elif Is_Image_File==111:
        return send_file(chatRoomimages)
    else: 
        return {
            'url': 'image_see',
            'data': {},
            'type': '失败',
            'message': '图像文件不存在',
            'Time': glode.NowTime(),  # 根据需要修改为当前时间
        }
