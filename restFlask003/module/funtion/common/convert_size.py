def convert_size(size_bytes):
    # 转换文件大小为常用数据格式
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    t=0
    for i in range(0,len(size_name),1):
        if(size_bytes>=1024):
            size_bytes=size_bytes/1024
            t=i
            size_bytes=int(size_bytes)
    return str(size_bytes)+size_name[t+1]