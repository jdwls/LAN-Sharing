export function Toker(data) {
  localStorage.setItem("UresName", data.Ures);
  localStorage.setItem("Authority", data.Authority);
  localStorage.setItem("Time", data.Time);
  if (
    localStorage.getItem("UresName") == "" ||
    localStorage.getItem("Authority") == "" ||
    localStorage.getItem("Time") == ""
  ) {
    return "存储失败";
  }
  return "存储成功";
}

export default Toker;
