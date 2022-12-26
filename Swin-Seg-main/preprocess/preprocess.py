import os
import cv2
import glob

def npz():
    #原图像路径
    path = 'C:/Users/tanyi/Swin-Seg-main/tools/blurred_mask/*.png'
    #path = 'C:/Users/tanyi/Swin-Seg-main/tools/Predict_mask_2017/*.png'
    for i, img_path in enumerate(glob.glob(path)):
        label = cv2.imread(img_path, flags=0)
        #将非目标像素设置为0
        label[label==0]=0
        #将目标像素设置为1
        label[label!=0]=1

        outpath = img_path.replace('blurred_mask', 'blurred_mask_eval')

        print('------------',i)
        cv2.imwrite(outpath, label)

    print('ok')

def main():
    npz()

if __name__ == '__main__':
    main()
