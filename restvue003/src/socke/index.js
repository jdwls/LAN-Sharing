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
  if (socket.connected) return;
  
  const username = localStorage.getItem('UresName');
  if (!username) {
    console.error('无法建立连接: 缺少用户名');
    return;
  }
  
  socket.auth = { username };
  socket.connect();
  
  socket.on('connect', () => {
    console.log('Socket连接成功');
    socket.emit("user_login", { username });
  });
  
  socket.on('online_users_update', (data) => {
    if (data.action === 'login') {
      if (!store.state.Online_Numbers.includes(data.username)) {
        store.state.Online_Numbers.push(data.username);
      }
    } else if (data.action === 'logout') {
      store.state.Online_Numbers = store.state.Online_Numbers.filter(
        user => user !== data.username
      );
    }
  });
  
  socket.on('current_online_users', (data) => {
    store.state.Online_Numbers = data.online_users;
  });
}

// 断开连接
export function disconnectSocket() {
  if (socket.connected) {
    socket.disconnect();
    console.log('Socket已断开');
  }
}

// 自动重连逻辑
socket.on('disconnect', (reason) => {
  console.log(`连接断开: ${reason}`);
  if (reason === 'io server disconnect') {
    socket.connect(); // 服务器主动断开时尝试重连
  }
});

// 错误处理
socket.on('connect_error', (err) => {
  console.error('连接错误:', err.message);
});

export default { connectSocket, disconnectSocket, socket };