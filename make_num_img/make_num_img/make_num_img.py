import cv2
import numpy as np
import os

def make_num_img(path,start_num=0,nfiles=10,sub_nfile=2,hight=100,width=200,extension="jpeg"):
    """path:作成パス, start_num:開始番号, nfiles:作成画像総数, sub_nfiles:サブフォルダ毎の画像数, hight:画像縦幅, width:画像横幅"""
    sub_fol_cnt=0
    os.makedirs(f"{path}\{str(sub_fol_cnt)}",exist_ok=True)
    for i in range(nfiles):
        img = np.ones([hight,width,3])*255
        cv2.putText(img,text=str(i+start_num),org=(0,int(hight/2)),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0, 0, 0),lineType=cv2.LINE_AA)
        cv2.imwrite(f"{path}\{str(sub_fol_cnt)}\{str(i+start_num)}.{extension}",img)
        if (i+1) % sub_nfiles == 0 and (i+1) != nfiles:
            sub_fol_cnt+=1
            os.makedirs(f"{path}\{str(sub_fol_cnt)}",exist_ok=True)


if __name__=="__main__":
    path=input("path:")
    start_num=int(input("start_num:"))
    nfiles=int(input("nfiles:"))
    sub_nfiles=int(input("sub_nfiles:"))
    hight=int(input("hight:")) 
    width=int(input("width:"))
    make_num_img(path,start_num,nfiles,sub_nfiles,hight,width)
