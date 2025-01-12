# routes/option_dir.py

from flask import Blueprint, jsonify
import os
import tkinter as tk
from tkinter import filedialog
from module.glode import glode
from module.funtion.common import readdirpath
import logging

# 创建蓝图对象
option_dir_blueprint = Blueprint('option_dir', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@option_dir_blueprint.route('/OptionDir', methods=['POST', 'GET'])
def OptionDir():
    dir_path = readdirpath.dirMOde(glode.dirpath())
    
    # 检查是否有有效目录
    if dir_path == '' or not os.path.exists(dir_path):
        logging.info("未找到有效目录，打开文件对话框以选择目录")
        
        # 创建隐藏的Tkinter根窗口
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", 1)

        # 打开文件选择对话框
        selected_dir = filedialog.askdirectory()
        root.destroy()

        if selected_dir:
            # 保存所选目录到文件
            with open(glode.dirpath(), 'w', encoding="utf-8") as f:
                f.write(selected_dir)

            # 记录操作日志
            with open(glode.dirPathLog(), 'a', encoding="utf-8") as f:
                log_entry = f"{glode.NowTime()}  选择目录: {selected_dir}\n"
                f.write(log_entry)
                logging.info(f"已记录选择的目录: {selected_dir}")

            return jsonify({
                'url': 'OptionDir',
                'data': readdirpath.dirMOde(glode.dirpath()),
                'type': '成功选择目录',
                'Time': glode.NowTime()
            }), 200  # 返回200状态码
        else:
            logging.warning("用户未选择目录")
            return jsonify({
                'url': 'OptionDir',
                'data': readdirpath.dirMOde(glode.dirpath()),
                'type': '未选择目录',
                'Time': glode.NowTime()
            }), 400  # 返回400状态码
    else:
        logging.info(f"已选择有效目录: {dir_path}")
        return jsonify({
            'url': 'OptionDir',
            'data': readdirpath.dirMOde(glode.dirpath()),
            'type': '已经选择目录',
            'Time': glode.NowTime()
        }), 200  # 返回200状态码
