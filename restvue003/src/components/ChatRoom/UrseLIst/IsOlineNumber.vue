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
    this.socket.open();
    this.socket.on("connect", () => {
      console.log("Connected to server");
    });
  },
  beforeUnmount() {
    this.socket.disconnect();
  },
};
</script>
