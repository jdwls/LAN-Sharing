import { io } from "socket.io-client";
import { store } from '@/store/index.js'
const socket = io(store.state.api, {
  autoConnect: false,
  transports: ["websocket"],
  reconnection: true,
  reconnectionAttempts: 5,
  reconnectionDelay: 1000,
  timeout: 10000
});

// 连接管理

export function connectSocket() {
  const username = localStorage.getItem('UresName');
  socket.connect();
  socket.on('connect', () => {
    socket.emit("user_login_chat_room", { username });
  });
}
// 断开连接
export function disconnectSocket() {

  socket.on('disconnect', () => {
    console.log('Socket disconnected');
  });
  socket.disconnect();
}
// 发送登录信息
export function updata_online_urse_list_fun() {
  socket.on('updata_online_urse_list', (after_return_urse_lists_data) => {
    store.state.Online_Numbers = []
    for (let i = 0; i < after_return_urse_lists_data.online_users.length; i++)
      if (after_return_urse_lists_data.online_users[i].user_name !== localStorage.getItem('UresName'))
        store.state.Online_Numbers.push(after_return_urse_lists_data.online_users[i].user_name)
  });
}
export function disconnect_user_list_fun() {
  socket.on('disconnect_user_lists', (after_return_disconnect_user_list_data) => {
    let online_connect_user_list = [];
    online_connect_user_list = [...store.state.Online_Numbers]
    online_connect_user_list.push(localStorage.getItem('UresName'))
    store.state.disconnectNumber = after_return_disconnect_user_list_data.filter((item => {
      return !online_connect_user_list.includes(item)
    }))
  })
}
export function seend_message_fun(ms, report_name,ms_index) {
  socket.emit('seend_message_data', { 
    'message_index':ms_index+1,
    'message_type':'text',
    'message': ms, 
    'send_name': localStorage.getItem('UresName'), 
    'report_name': report_name, 
    'Time': new Date().getTime(),
    'read_state':false,
    'current_usrs':true,
    'revocation_or_drop':{
      'drop':{
        'drop_name':[0,0],
        'drop_state':[true,true]
      },
      'revocation':{
        'revocation_name':null,
        'revocation_state':true
      }
    }
  });
}
export function after_seend_message_fun(){
  socket.on('after_seend_message_data',((res)=>{
    if (res.send_name==localStorage.getItem('UresName'))
      res.current_usrs=true
    else{
      res.current_usrs=false
    }
    store.state.messages_lists.push(res);
  })) 
}
export function emit_revocation_message_socket_fun(message_index, sned_user_name, report_name) {
  socket.emit('revocation_message_socket', { 'message_index': message_index, 'send_name': sned_user_name, 'report_name': report_name });
}
export function on_revocation_message_socket_fun(){
  socket.on('after_revocation_message_socket',((res)=>{
   store.state.messages_lists=res
  }))
}
export function seend_message_Files_fun(file_name, report_name,message_index,file_type){
  socket.emit('seend_message_Files_socket', { 
    'message_index':message_index+1,
    'message_type':file_type,
    'message': [file_name,'fileUrl'],
    'send_name': localStorage.getItem('UresName'), 
    'report_name': report_name, 
    'Time': new Date().getTime(),
    'read_state':false,
    'current_usrs':true,
    'revocation_or_drop':{
      'drop':{
        'drop_name':[0,0],
        'drop_state':[true,true]
      },
      'revocation':{
        'revocation_name':null,
        'revocation_state':true
      }
    }
  });
}
export function on_message_Files_fun(){
socket.on('after_message_Files_socket',((res)=>{
   store.state.messages_lists=res
  }))
}
// 检测连接状态
on_message_Files_fun()
updata_online_urse_list_fun();
disconnect_user_list_fun()
after_seend_message_fun()
on_revocation_message_socket_fun()
export default { connectSocket, disconnectSocket, socket, seend_message_fun,emit_revocation_message_socket_fun,seend_message_Files_fun };