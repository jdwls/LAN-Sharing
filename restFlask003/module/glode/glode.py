import datetime
import json
def asfliezip():
    return 'restFlask003/template/flieZip'
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
    fileypesss = ['.pdf', '.docx', '.xlsx','.jpg', '.png', '.gif', '.txt', '.mp4', '.json','.bmp']
    return fileypesss
def fileypesss2():
    fileypesss2 = [{'.pdf':'application/pdf'}, {'.docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'},{'.xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}, {'.jpg':'image/jpeg'}, {'.png':'image/png'}, {'.gif':'image/gif'}, {'.txt':'text/plain'}, {'.mp4':'video/mp4'},{'.json':'application/json'}, {'.bmp':'image/bmp'}]
    return fileypesss2
def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]
def UresPathJson():
    UresPathJson = 'restFlask003/template/uresAndAdmin/ures.json'
    return UresPathJson
def AdminPathJson():
    AdminPathJson = 'restFlask003/template/uresAndAdmin/admin.json'
    return AdminPathJson
def IsOlineNumbers():
    IsOlineNumbers = 'restFlask003/template/commoon/IsOlineNumber.json'
    return IsOlineNumbers
def read_char_list(path):
    with open(path,'r',encoding='utf-8') as f:
        read_char_list_json=json.load(f)
        f.close()
    return read_char_list_json
def write_char_list(read_char_list_json,res,path):
    try:
        read_char_list_json.append(res)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(read_char_list_json, f, ensure_ascii=False, indent=4)
            f.close()
        return True
    except Exception as e:
        print(f"写入聊天记录失败: {e}")
        return False