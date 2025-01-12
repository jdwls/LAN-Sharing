import os
from module.funtion import readdirpath
from module.glode import glode

def isFileType(path):
   if(os.path.isdir(readdirpath.dirMOde(glode.dirpath())+'/'+path)==True):
       return True
   else:
      return False