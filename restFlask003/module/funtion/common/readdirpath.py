def dirMOde(dirpath):
    with open(dirpath, encoding="utf-8") as f:
        dirpathValue = f.read()
        f.close()
    return dirpathValue
