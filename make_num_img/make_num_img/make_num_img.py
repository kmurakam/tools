import cv2
import numpy as np
import os

def make_num_img(path,start_num=0,nfiles=10,sub_nfile=2,hight=100,width=200,extension="jpeg"):
    """path:作成パス, start_num:開始番号, nfiles:作成画像総数, sub_nfiles:サブフォルダ毎の画像数, hight:画像縦幅, width:画像横幅"""
    sub_fol_cnt=0 #サブフォルダの番号
    os.makedirs(f"{path}\{str(sub_fol_cnt)}",exist_ok=True)
    for i in range(nfiles):
        img = np.ones([hight,width,3])*255 #白画像作成
        cv2.putText(img,text=str(i+start_num),org=(0,int(hight/2)),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.0,color=(0, 0, 0),lineType=cv2.LINE_AA)

        cv2.imwrite(f"{path}\{str(sub_fol_cnt)}\{str(i+start_num)}.{extension}",img)
        if (i+1) % sub_nfiles == 0 and (i+1) != nfiles: #出力した画像数がサブフォルダ毎の画像数の倍数かつ一番最後でない場合
            sub_fol_cnt+=1
            os.makedirs(f"{path}\{str(sub_fol_cnt)}",exist_ok=True)


if __name__=="__main__":
    path=input("作成パス：")
    start_num=int(input("開始番号："))
    nfiles=int(input("作成画像総数："))
    sub_nfiles=int(input("サブフォルダ毎の画像数："))
    hight=int(input("画像縦幅：")) 
    width=int(input("画像横幅："))
    make_num_img(path,start_num,nfiles,sub_nfiles,hight,width)
