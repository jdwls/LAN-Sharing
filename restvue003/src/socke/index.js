import { io } from "socket.io-client";
import { store } from "@/store/index.js";
// 创建socket实例（注意：生产环境应使用HTTPS）
export const socket = io("ws://localhost:2525", {
  autoConnect: false,
  transports: ["websocket"],
});
// 连接Socket并设置事件监听
export function connectSocket() {
  socket.connect(); // 必须手动连接
  socket.on("connect", () => {
    console.log("Socket connected");
  });
  socket.on("disconnect", () => {
    console.log("Socket disconnected");
  });
  socket.on("connect_error", (error) => {
    console.error("Connection error:", error);
  });
}
// 发送消息
export function sendMessage() {
  socket.emit("message", "zhuj");
}
// 获取在线人数（需要后端配合）
export function requestOnlineNumbers() {
  socket.on("Online_Numbers", (res) => {
    setInterval(async () => {
      store.state.Online_Numbers = await res["name"];
    });
    return store.state.Online_Numbers;
  });
  return store.state.Online_Numbers;
}
export function disconnectNumber() {}
export default {
  connectSocket,
  sendMessage,
  requestOnlineNumbers,
  socket,
};
