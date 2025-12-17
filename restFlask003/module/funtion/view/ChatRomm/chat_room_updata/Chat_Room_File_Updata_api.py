from flask import Blueprint, request, send_file, jsonify, make_response
import os
import shutil
from pathlib import Path
from flask_cors import CORS
import logging
import module.glode.glode as glode
import json
from threading import Lock
from copy import deepcopy
# 创建蓝图对象
Chat_Room_File_Updata_api_blueprint = Blueprint('Chat_Room_File_Updata_api_blueprint', __name__)
CORS(Chat_Room_File_Updata_api_blueprint, supports_credentials=True)
# 配置日志
logging.basicConfig(level=logging.INFO, filename='app.log',
                    filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
file_lock = Lock()
@Chat_Room_File_Updata_api_blueprint.route('/Chat_Room_File_Updata_api', methods=['GET','POST'])
def Chat_Room_File_Updata_api():
    original_chat_room_list=[]
    formData= request.files['file']
    file_name= request.form.get('file_name')
    FileS_Types=json.loads(request.form.get('FileS_Types'))
    send_name= request.form.get('send_name')
    report_name= request.form.get('report_name')
    Time=request.form.get('Time')
    FileS_name_arr=json.loads(request.form.get('FileS_name_arr'))
    # print(len(FileS_name_arr))
    revocation_or_drop={
      'drop':{
        'drop_name':[0,0],
        'drop_state':[True,True]
      },
      'revocation':{
        'revocation_name':None,
        'revocation_state':True
      }
    }
    sort_data=[send_name,report_name]
    try:
        if file_name:
            sort_data= sorted(sort_data)
            send_name_to_report_name_path = os.path.join(glode.path(),'template/char_list',f"{sort_data[0]}_to_{sort_data[1]}")
            send_name_to_report_name_File_path = os.path.join(send_name_to_report_name_path,file_name)
            os.makedirs(os.path.dirname(send_name_to_report_name_File_path), exist_ok=True) 
            formData.save(send_name_to_report_name_File_path)
            send_name_to_report_File_path=os.path.join(glode.path(),'template/char_list',f"{sort_data[0]}_to_{sort_data[1]}.json")
            # send_name_to_report_name_path= os.path.join(glode.path()+'template/char_list/'+sort_data[0]+'_to_'+sort_data[1]+'.json') 
        else:
            return jsonify({'error': '文件上传失败'}), 200 
        if not os.path.exists(send_name_to_report_File_path):
            with open(send_name_to_report_File_path,'w',encoding='utf-8') as f:
                json.dump([],f, ensure_ascii=False, indent=4)
        if FileS_name_arr!=False:
    
            data={
                'message_index':'',
                'message_type':'',
                'message':[file_name],
                'send_name':send_name,
                'report_name':report_name,
                'Time':Time,
                'read_state':False,
                'revocation_or_drop':revocation_or_drop
                
                } 
            with open(send_name_to_report_File_path,'r',encoding='utf-8') as f:
                chat_room_lists=json.load(f)
                f.close()
                
            for i in range(0,len(FileS_name_arr),1):
                send_name_to_report_name_File_path = os.path.join(send_name_to_report_name_path,FileS_name_arr[i])
                print(send_name_to_report_name_File_path,i,'----------------------------------------------------------')
                # print(str(len(chat_room_lists)+i+1))
                data_copy =deepcopy(data) 
                data_copy['message_index']=str(len(chat_room_lists)+i+1)
                data_copy['message_type']=FileS_Types[i]
                # data_copy['message'][1]=send_name_to_report_name_File_path
                data_copy['message'][0]=FileS_name_arr[i]
                data_copy['send_name_to_report_name_File_path']=os.path.join('//template\\char_list',f"{sort_data[0]}_to_{sort_data[1]}",FileS_name_arr[i])
                original_chat_room_list.append(data_copy)
            for i in range(len(original_chat_room_list)):
                chat_room_lists.append(original_chat_room_list[i])
            with open(send_name_to_report_File_path,'w',encoding='utf-8') as f:
                json.dump(chat_room_lists,f, ensure_ascii=False, indent=4)
            return '成功'    
        return '1'
    except Exception as e:
        return str(e)
       