'''
此代码是查找出一个文件夹里面，
所有图片读取错误，再删除
'''
import os
import shutil
import warnings
import cv2
import io
from PIL import Image
warnings.filterwarnings("error", category=UserWarning)
base_dir = "C:/Users/tanyi/Swin-Seg-main/tools/data/ade/ADEChallengeData2016/annotations/training"#删除图片的根目录
i = 0
def is_read_successfully(file):
    try:
        imgFile = Image.open(file)#这个就是一个简单的打开成功与否
        return True
    except Exception:
        return False
for parent, dirs, files in os.walk(base_dir):#(root,dirs,files)
    for file in files:
        if not is_read_successfully(os.path.join(parent, file)):
            print(os.path.join(parent, file))
            #os.remove(os.path.join(parent, file)) #真正使用时，这一行要放开，自己一般习惯先跑一遍，没有错误了再删除，防止删错。
            i = i + 1
print(i)
