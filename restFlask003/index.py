from flask import Flask, render_template,request,Response,send_from_directory,send_file,Blueprint
from flask_cors import CORS
import webbrowser
import os
from module.funtion.view.File_Updata.function.OptionDir import option_dir_blueprint
from module.funtion.view.File_Updata.function.upload import upload_bp 
from module.funtion.view.File_Updata.function.uploads import upload_bps
from module.funtion.view.File_Updata.function.selectedDir import selectedDir_blueprint
from module.funtion.view.File_Updata.function.SucceedselectedDir import SucceedselectedDir_blueprint
from module.funtion.view.File_Updata.DirsFileList import DirsFileList_blueprint
from module.funtion.view.File_Updata.function.NewDir import NewDir_blueprint
from module.funtion.view.File_Updata.function.download import download_blueprint
from module.funtion.view.File_Updata.function.drop import drop_blueprint
from module.funtion.view.File_Updata.function.OpenDir import OpenDir_blueprint
from module.funtion.view.File_Updata.function.openDirs import openDirs_blueprint
from module.funtion.view.File_Updata.function.TopLevelDirectory import TopLevelDirectory_blueprint
from module.funtion.view.File_Updata.function.office import office_blueprint
from module.funtion.view.File_Updata.function.fileypess import fileypess_blueprint
from module.funtion.view.File_Updata.function.filesypess import filesypess_blueprint
from module.funtion.see.VideoPlay import video_play_blueprint
from module.funtion.see.imageSee import imagesee_blueprint
from module.funtion.see.textSee import textsee_blueprint
from module.funtion.view.File_Updata.function.getDirs import getDirs_blueprint
from module.funtion.view.File_Updata.function.TextLnsert import TextLnsert_blueprint
from module.funtion.view.Login.login import login_blueprint
from module.funtion.view.Logup.Logup import Logup_blueprint
from module.funtion.view.Torken.Cookie import Cookie_blueprint
from module.funtion.view.Torken.Toker import Toker_blueprint
from module.funtion.view.ChatRomm.UreList import UreList_blueprint
from module.funtion.view.ChatRomm.Socket.IsOlineNumber import socketio
from module.funtion.view.ChatRomm.Socket.IsOlineNumber import IsOlineNumber_blueprint
from flask_socketio import SocketIO,send,emit
from module.glode.glode import path
from module.funtion.view.ChatRomm.after_chat_information_list import after_chat_information_list_blueprint
from module.funtion.view.ChatRomm.Drop_message_api import Drop_message_api_blueprint
app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='static')
CORS(app)
socketio.init_app(app, cors_allowed_origins="*")
app.register_blueprint(UreList_blueprint)
app.register_blueprint(Drop_message_api_blueprint)
app.register_blueprint(after_chat_information_list_blueprint)
app.register_blueprint(IsOlineNumber_blueprint)
app.register_blueprint(option_dir_blueprint)
app.register_blueprint(Toker_blueprint)
app.register_blueprint(Cookie_blueprint)
app.register_blueprint(fileypess_blueprint)
app.register_blueprint(upload_bp)
app.register_blueprint(upload_bps)
app.register_blueprint(selectedDir_blueprint)
app.register_blueprint(DirsFileList_blueprint)
app.register_blueprint(NewDir_blueprint)
app.register_blueprint(SucceedselectedDir_blueprint)
app.register_blueprint(drop_blueprint)
app.register_blueprint(OpenDir_blueprint)
app.register_blueprint(office_blueprint)
app.register_blueprint(TopLevelDirectory_blueprint )
app.register_blueprint(download_blueprint)
app.register_blueprint(openDirs_blueprint)
app.register_blueprint(filesypess_blueprint)
app.register_blueprint(video_play_blueprint)
app.register_blueprint(imagesee_blueprint)
app.register_blueprint(textsee_blueprint)
app.register_blueprint(getDirs_blueprint)
app.register_blueprint(TextLnsert_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(Logup_blueprint)
webbrowser.open_new('http://localhost:2525')
# 开启首页文件位置
@app.route('/',methods=['post', 'get'])
def hello_world():
    os.system(path()+'template/CMD/dropdowln.bat')
    return render_template('index.html')
# @socketio.on('connect')
# def handle_connect():
#     print('客户端连接成功')
# @socketio.on('Toker')
# def Toker(data):
#     print('接收到的用户名:', data)
if __name__ == '__main__': 
   print(app.url_map)
   app.run(host='0.0.0.0',port=2525,debug=True)
#    ssl_context=('template/crt/localhost.crt', 'template/crt/localhost.key')
   