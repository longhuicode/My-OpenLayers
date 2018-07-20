import urllib.request
import os
import time

# 文件存放目录
targetDir = r".\svg"

def destFile(path):  
    if not os.path.isdir(targetDir):  
        os.mkdir(targetDir)  
    pos = path.rindex('/')  
    t = os.path.join(targetDir, path[pos+1:])  
    return t 

def save_img(img_url):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 svg 文件夹
    #下载图片，并保存到文件夹中
    urllib.request.urlretrieve(img_url, destFile(img_url))

if __name__ == '__main__':
    img_urlROD = 'http://192.168.200.120:8180/svg/{0}.svg'
    for x in range(100000):
        print(x)
        img_url = img_urlROD.format(x)
        print(img_url)
        try:
            save_img(img_url)
        except Exception as e:
            print(e)
        