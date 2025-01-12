def asfliezip():
    return './template/as/path/asfliezip'
def dirpath():
    return './template/as/path/dirPath.txt'
def dirPathLog():
    dirPathLog='./template/as/path/dirPathLog.txt'
    return dirPathLog
def LishiPath():
    LishiPath='./template/as/path/dirPath.txt'
    
    return LishiPath
import datetime
def NowTime():
    NowTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return NowTime
def fileypesss():
    fileypesss = ['.pdf','.docx','.xlsx','.jpg','.png','.gif','.txt','.mp4']
    return fileypesss
def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]
