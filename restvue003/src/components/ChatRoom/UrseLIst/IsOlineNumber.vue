<template>
  <div>11</div>
</template>

<script>
import { io } from "socket.io-client";
export default {
  data() {
    return {
      socket: io(this.$store.state.api, {
        autoConnect: false,
      }),
    };
  },
  name: "IsOlineNumber",
  mounted() {
    //   this.socket.open();
    //   this.socket.on("connect", () => {
    //     console.log("Connected to server");
    //     this.socket.emit("OnlineSendNumber", {
    //       name: localStorage.getItem("UresName"),
    //     });
    //     this.socket.on("ReceiveNumber", (data) => {
    //       console.log("ReceiveNumber", data);
    //     });
    //   });
    // },
    // beforeUnmount() {
    //   this.socket.emit("DisconnectSendNumber", {
    //     name: localStorage.getItem("UresName"),
    //   });
    //   this.socket.disconnect();
  },
};
</script>
