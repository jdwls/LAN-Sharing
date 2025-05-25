import datetime


def asfliezip():
    return '/template/as/path/asfliezip'


def dirpath():
    return './restFlask003/template/as/path/dirPath.txt'


def dirPathLog():
    dirPathLog = './restFlask003/template/as/path/dirPathLog.txt'
    return dirPathLog


def LishiPath():
    LishiPath = './restFlask003/template/as/path/dirPath.txt'

    return LishiPath


def NowTime():
    NowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return NowTime


def fileypesss():
    fileypesss = ['.pdf', '.docx', '.xlsx','.jpg', '.png', '.gif', '.txt', '.mp4']
    return fileypesss

def fileypesss2():
    fileypesss2 = [{'.pdf':'application/pdf'}, {'.docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'},{'.xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}, {'.jpg':'image/jpeg'}, {'.png':'image/png'}, {'.gif':'image/gif'}, {'.txt':'text/plain'}, {'.mp4':'video/mp4'}]
    return fileypesss2
def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]
