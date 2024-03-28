from flask import Flask, render_template,request,Response,send_from_directory,send_file
from flask_cors import CORS
import webbrowser
import tkinter as tk
import os
from tkinter import filedialog
import datetime
import shutil

# static_folder='./dist'

dirpath='restFlask003/template/as/path/dirPath.txt'
LishiPath='restFlask003/template/as/path/LishiPath.txt'
dirPathLog='restFlask003/template/as/path/dirPathLog.txt'
asfliezip='restFlask003/template/as/asfliezip'
def dirMOde():
    with open(dirpath ,encoding="utf-8") as f:
         dirpathValue=f.read()
         f.close()
         return dirpathValue
def convert_size(size_bytes):
    # 转换文件大小为常用数据格式
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    t=0
    for i in range(0,len(size_name),1):
        if(size_bytes>=1024):
            size_bytes=size_bytes/1024
            t=i
            size_bytes=int(size_bytes)
    return str(size_bytes)+size_name[t+1]
def isFileType(path):
   if(os.path.isdir(dirMOde()+'/'+path)==True):
       return True
   else:return False
NowTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# app = Flask(__name__, instance_relative_config=True, template_folder='./dist',static_url_path="",static_folder='./dist')

app = Flask(__name__, instance_relative_config=True, template_folder='./template',static_folder='./template')
CORS(app)
fileypesss = ['.pdf','.docx','.xlsx','.jpg','.png','.gif','.txt','.mp4']
webbrowser.open_new('http://localhost:2525')
# 开启首页文件位置
@app.route('/',methods=['post', 'get'])
def hello_world():
   os.system('./template/as/dropdowln.bat')
   return render_template('index.html')
#    return send_from_directory('./dist', 'index.html')
@app.route('/OptionDir',methods=['post','get'])
def OptionDir():
    if(dirMOde()=='' or os.path.exists(dirMOde())==False):
      root = tk.Tk()
      root.withdraw()
      root.attributes("-topmost",1)
      Dirs = filedialog.askdirectory()
      root.destroy()
      if(Dirs!=''):
         with open(dirpath,'w' ,encoding="utf-8") as f:
            f.write(Dirs)
            f.close()
         with open(dirPathLog,'a' ,encoding="utf-8") as f:
            f.write(NowTime)
            f.write('        ')
            f.write(Dirs)
            f.write('/n')
            f.close()
         return {
            'url':'OptionDir',
            'data':dirMOde(),
            'type':'成功选择目录',
            'Time':NowTime
         }
      else:return{
            'url':'OptionDir',
            'data':dirMOde(),
            'type':'未选择目录',
            'Time':NowTime
      }
    else:return{
            'url':'OptionDir',
            'data':dirMOde(),
            'type':'已经选择目录',
            'Time':NowTime
      }
@app.route('/uploader',methods=['post', 'get'])
def uploader():
   with open(dirpath,encoding="utf-8") as f:
    data=f.read()
   if request.method == 'POST':
      f = request.files['file']
      basepath = os.path.dirname(__file__)
      upload_path = os.path.join(basepath, data, f.filename)
      f.save(upload_path)
      response ='文件上传成功'
      if response=='文件上传成功':
            with open(dirPathLog,'a' ,encoding="utf-8") as f:
               f.write(NowTime)
               f.write('        ')
               f.write('保存文件：'+request.files['file'].filename+"      ")
               f.write('保存路径：'+data)
               f.write('/n')
               f.close()
            return{
            'url':'uploader',
            'data':request.files['file'].filename,
            'type':'文件',
            'Time':NowTime,
            'iss':'文件上传成功'
      }
      else: return{
            'url':'uploader',
            'data':request.files['file'].filename,
            'type':'文件',
            'Time':NowTime,
            'iss':'文件上传失败'
            }
@app.route('/uploaders',methods=['post', 'get'])
def uploaders():
   uploadpath=request.form['uploadpath']
   print(uploadpath)
   if 'file' not in request.files:
        with open(dirPathLog,'a' ,encoding="utf-8") as f:
               f.write(NowTime)
               f.write('        ')
               f.write(uploadpath+'/'+request.files['file'].filename+"     "+"目录没有上传")
               f.write('/n')
               f.close()
         # 获取文件大小
        return {
            "url":'/uploaders',
            "data":request.files['file'].filename,
            "type":'上传目录',
            "Time":NowTime,
             'iss':'目录没有上传',
            
        }
   files = request.files.getlist('file')
   for file in files:
        if file.filename == '':
            with open(dirPathLog,'a' ,encoding="utf-8") as f:
               f.write(NowTime)
               f.write('        ')
               f.write(uploadpath+'/'+request.files['file'].filename+"     "+"没有选择目录")
               f.write('/n')
               f.close()
            return {
            "url":'/uploaders',
            "data":request.files['file'].filename,
            "type":'上传目录',
            "Time":NowTime,
             'iss':'没有选择目录'
            }
        if file:
           
            # 获取文件的路径
            path = os.path.join(uploadpath, file.filename)
            print(path)
            # 创建文件的目录
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # 保存文件
            file.save(path)
            uploaded_file = request.files['file']  # 假设前端上传的文件字段名为 'file'
            file_size = len(uploaded_file.read()) 
            with open(dirPathLog,'a' ,encoding="utf-8") as f:
               f.write(NowTime)
               f.write('        ')
               f.write(uploadpath+'/'+request.files['file'].filename+"     "+"目录上传成功")
               f.write('/n')
               f.close()
   return {
            "url":'/uploaders',
            "data":request.files['file'].filename,
            "type":'上传目录',
            "Time":NowTime,
             'iss':'目录上传成功',
              "Filesize": str(convert_size(request.content_length))
            }
@app.route('/selectedDir',methods=['post', 'get'])
def selectedDir():
   root = tk.Tk()
   root.withdraw()
   root.attributes("-topmost",1)
   Dirs = filedialog.askdirectory()
   root.destroy()
   if Dirs:
       with open(dirpath ,'w',encoding="utf-8") as f:
            f.write(Dirs)
            f.close()
       with open(dirPathLog,'a' ,encoding="utf-8") as f:
            f.write(NowTime)
            f.write('        ')
            f.write("选择目录多少没有确定:"+Dirs)
            f.write('/n')
            f.close()
   return{
        'url':'OptionDir',
         'data':Dirs,
         'type':'已经选择目录',
         'Time':NowTime
    }
@app.route('/SucceedselectedDir',methods=['post', 'get'])
def SucceedselectedDir():
    dirname=request.args.get('dirname')
    print(dirname)
    with open(dirpath,'w' ,encoding="utf-8") as f:
            f.write(dirname)
            f.close()
    with open(dirPathLog,'a' ,encoding="utf-8") as f:
            f.write(NowTime)
            f.write('        ')
            f.write("确定路径:"+dirMOde())
            f.write('/n')
            f.close()
    return {
           'url':'SucceedselectedDir',
            'data':dirMOde(),
            'type':'确定路径',
            'Time':NowTime
    }
@app.route('/DirsFileList',methods=['post', 'get'])
def DirsFileList():
     DirsFileList=request.args.get('DirsFileList')
     if(DirsFileList=='no'):
      return{
         'url':'DirsFileList',
            'data':os.listdir(dirMOde()),
            'type':'当前目录下的所有文件和文件夹',
            'Time':NowTime
      }
     else:
        print(DirsFileList)
        return{
         'url':'DirsFileList',
            'data':os.listdir(DirsFileList),
            'type':'当前目录下的所有文件和文件夹',
            'Time':NowTime
      }
@app.route('/NewDir',methods=['post', 'get'])
def NewDir():
    NewDirName = request.args.get('NewDirName')
    NewDirPath=request.args.get('NewDirPath')
    if os.path.exists(NewDirPath+'/'+NewDirName):  
         return '文件存在'
    else: 
        os.makedirs(NewDirPath+'/'+NewDirName)
        with open(dirPathLog,'a' ,encoding="utf-8") as f:
            f.write(NowTime)
            f.write('        ')
            f.write('新建文件夹:'+NewDirPath+'/'+NewDirName)
            f.write('/n')
            f.close()
        return '成功'
@app.route('/download')
def download():
     downloadName = request.args.get('downloadName')
     downloadPathName= request.args.get('downloadPathName')
     if(os.path.isdir(downloadPathName)==False):
          print(downloadName,downloadPathName)
          return send_file(downloadPathName,as_attachment=True)
     elif(os.listdir(downloadPathName)!=[]):
         shutil.make_archive(asfliezip+'/'+downloadName,'zip',downloadPathName)
         downloads=send_file(asfliezip+'/'+downloadName+'.zip', as_attachment=True)
         os.system('E:/备份/桌面/代码/代码/restFlask003/template/as/dropdowln.bat')
         return  downloads
     else:
         return{
         'url':'download',
         'data':'',
         'type':'空',
         'Time':NowTime
         }
@app.route('/dropFiles')
def dropFiles():
    dirse=request.args.get('dropFilesName')
    if(os.path.isdir(dirse)==True):
      shutil.rmtree(dirse)
      return{
        'url':'dropFiles',
         'data':dirse,
         'type':'删除文件夹成功',
         'Time':NowTime
    }
    else:
        os.remove(dirse)
        return{
        'url':'dropFiles',
         'data':dirse,
         'type':'删除文件成功',
         'Time':NowTime
    }
    return{
        'url':'dropFiles',
         'data':dirse,
         'type':'失败',
         'Time':NowTime
    }
@app.route('/OpenDir',methods=['post','get'])
def OpenDir():
   type={}
   j=1
   dir=os.listdir(dirMOde())
   lens=len(dir)
   for i in range(0,lens,1):
      if(os.path.isdir(dirMOde()+'/'+dir[i])==True):
         type[j]=dir[i]
         j=j+1
   return {
      'su':type
   }
@app.route('/openDirs',methods=['post','get'])
def openDirs():
    dirs=request.args.get('OpenDirsName')
    type={}
    j=1
    dir=os.listdir(dirs)
    lens=len(dir)
    for i in range(0,lens,1):
      if(os.path.isdir(dirs+'/'+dir[i])==True):
         type[j]=dir[i]
         j=j+1  
    return {
        'url':'openDirs',
        'data':os.listdir(dirs),
        'type':'成功',
        'Time':NowTime,
        'dirName':dirs,
        'su':type
    }
@app.route('/TopLevelDirectory',methods=['post','get'])
def TopLevelDirectory():
    TopLevelDirectoryPathName=request.args.get('TopLevelDirectoryPathName')
    if(TopLevelDirectoryPathName!='E:'):
      print(TopLevelDirectoryPathName)
      TopLevelDirectoryPathName=TopLevelDirectoryPathName.split('/')
      s=TopLevelDirectoryPathName.pop()
      result = "/".join(TopLevelDirectoryPathName)
      return {
        'url':'TopLevelDirectory',
        'data':result,
        'type':'成功',
        'Time':NowTime,
       }
    else:
        return{
         'url':'TopLevelDirectory',
        'data':TopLevelDirectoryPathName,
        'type':'失败',
        'Time':NowTime,
        }
@app.route('/office',methods=['post','get'])
def office():
    uploadpath=request.args.get('dw')
    return send_file(uploadpath)
@app.route('/fileypess',methods=['post','get'])
def fileypess():
   ViewButtonOfficEword=request.args.get('ViewButtonOfficEword')
   for i in range(0,len(fileypesss),1):
       if(ViewButtonOfficEword.endswith(fileypesss[i])==True):
            return {
                 'url':'fileypess',
                  'data':fileypesss[i],
                  'type':'成功',
                  'Time':NowTime,
            }
   return {
                 'url':'fileypess',
                  'data':ViewButtonOfficEword,
                  'type':'失败',
                  'Time':NowTime,
            }  
@app.route('/filesypess',methods=['post','get'])
def filesypess():
    filesypessPath=request.args.get('filesypessPath')
    filesypessPathlist=os.listdir(filesypessPath)
    filesypessPathlistType={}
    filesypessPathlistTypes={}
    for i in range(0,len(filesypessPathlist),1):
      filesypessPathlistpath=filesypessPath+"/"+filesypessPathlist[i]
      for j in range(0,len(fileypesss),1):
         if(filesypessPathlistpath.endswith(fileypesss[j])==True):
            filesypessPathlistType[i]=fileypesss[j]
            filesypessPathlistTypes[i]={'index':i,'filesypessPathlistType':'查看文件'}
            break
         else:filesypessPathlistType[i]=False
    return { 'url':'filesypess',
           'data':filesypessPathlistType,
           'filesypessPathlistTypes':filesypessPathlistTypes,
          'type':'成功',
          'test':filesypessPathlist,
               'Time':NowTime,
          }
@app.route('/VideoPlay',methods=['post','get'])
def VideoPlay():
    VideoPlay=request.args.get('VideoPlay')
    return send_file(VideoPlay)
@app.route('/imageSee',methods=['post','get'])
def imageSee():
    imageSeeName=request.args.get('imageSeeName')
    return send_file(imageSeeName)
@app.route('/textSee',methods=['post','get'])
def textSee():
    textSee=request.args.get('textSee')
    return send_file(textSee)
@app.route('/filesgetsize',methods=['post','get'])
def filesgetsize():
    # filesgetsize=request.args.get('filesgetsize')
    return str(os.path.getsize(dirMOde()+'/开放日.zip'))
if __name__ == '__main__': 
   print(app.url_map)
   # 获取路由
   # app.config['X_SENDFILE_TYPE'] = 'X-Accel-Redirect'
   app.run(host='0.0.0.0',port=2525,)
   