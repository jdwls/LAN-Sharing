from flask import Blueprint, jsonify
import tkinter as tk
from tkinter import filedialog
from module.glode import glode  # 假设 glode 是自定义模块
import logging
import os

# 创建蓝图对象
selectedDir_blueprint = Blueprint('selectedDir_blueprint', __name__)

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@selectedDir_blueprint.route('/selectedDir', methods=['POST', 'GET'])
def selectedDir():
    # 创建一个 Tkinter 窗口以选择目录
    root = tk.Tk()
    root.withdraw()  # 隐藏 Tkinter 主窗口
    root.attributes("-topmost", 1)  # 窗口置顶

    # 打开文件夹选择对话框
    selected_dir = filedialog.askdirectory()  
    root.destroy()  # 选择目录后销毁 Tkinter 主窗口

    # 检查用户是否选择了目录
    if selected_dir:
        # 将选择的目录路径写入文件（覆盖现有内容）
        try:
            dir_path = glode.dirpath()
            if dir_path is None:
                logging.error("glode.dirpath() 返回 None")
                return jsonify({
                    'url': 'selectedDir',
                    'data': None,
                    'type': '失败',
                    'message': '获取目录路径时出错',
                    'Time': glode.NowTime()
                }), 500  # 返回500状态码

            # 检查路径是否有效
            if not os.path.exists(os.path.dirname(dir_path)):
                os.makedirs(os.path.dirname(dir_path))  # 创建目录

            with open(dir_path, 'w', encoding="utf-8") as f:
                f.write(selected_dir)

            # 将选择记录写入日志文件
            log_entry = f"{glode.NowTime()}  选择的目录路径: {selected_dir}\n"
            log_path = glode.dirPathLog()
            with open(log_path, 'a', encoding="utf-8") as f:
                f.write(log_entry)

            logging.info(f"选择的目录已记录: {selected_dir}")

            return jsonify({
                'url': 'selectedDir',
                'data': selected_dir,
                'type': '成功',
                'message': '已经选择目录',
                'Time': glode.NowTime()
            }), 200  # 返回200状态码

        except Exception as e:
            logging.error(f"写入目录路径或日志时发生错误: {e}")
            return jsonify({
                'url': 'selectedDir',
                'data': None,
                'type': '失败',
                'message': '保存目录路径时出错',
                'Time': glode.NowTime()
            }), 500  # 返回500状态码

    logging.warning("用户未选择任何目录")
    return jsonify({
        'url': 'selectedDir',
        'data': None,
        'type': '失败',
        'message': '未选择目录',
        'Time': glode.NowTime()
    }), 400  # 返回400状态码
