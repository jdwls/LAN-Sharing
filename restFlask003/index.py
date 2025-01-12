from flask import Flask, render_template,request,Response,send_from_directory,send_file,Blueprint
from flask_cors import CORS
import webbrowser
import os
from module.funtion.view.OptionDir import option_dir_blueprint
from module.funtion.view.upload import upload_bp 
from module.funtion.view.uploads import upload_bps
from module.funtion.view.selectedDir import selectedDir_blueprint
from module.funtion.view.SucceedselectedDir import SucceedselectedDir_blueprint
from module.funtion.view.DirsFileList import DirsFileList_blueprint
from module.funtion.view.NewDir import NewDir_blueprint
from module.funtion.view.download import download_blueprint
from module.funtion.view.drop import drop_blueprint
from module.funtion.view.OpenDir import OpenDir_blueprint
from module.funtion.view.openDirs import openDirs_blueprint
from module.funtion.view.TopLevelDirectory import TopLevelDirectory_blueprint
from module.funtion.view.office import office_blueprint
from module.funtion.view.fileypess import fileypess_blueprint
from module.funtion.view.filesypess import filesypess_blueprint
from module.funtion.see.VideoPlay import video_play_blueprint
from module.funtion.see.imageSee import imagesee_blueprint
from module.funtion.see.textSee import textsee_blueprint
from module.funtion.view.getDirs import getDirs_blueprint
from module.funtion.view.TextLnsert import TextLnsert_blueprint
from module.funtion.view.Login.login import login_blueprint
app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='static')
CORS(app)
app.register_blueprint(option_dir_blueprint)
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
webbrowser.open_new('http://localhost:2525')
# 开启首页文件位置
@app.route('/',methods=['post', 'get'])
def hello_world():
#    os.system('/template/as/dropdowln.bat')
    os.system('./template/as/dropdowln.bat')
    return render_template('index.html')
if __name__ == '__main__': 
   print(app.url_map)
   
   app.run(host='0.0.0.0',port=2525,debug=True)
   