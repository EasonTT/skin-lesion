import os
import cv2
import glob

def merge():
    #原图像路径
    outpath = 'C:/Users/tanyi/Swin-Seg-main/tools/union2017/'
    path1 = 'C:/Users/tanyi/Swin-Seg-main/tools/Predict_mask_2017/*.png'
    path2 = 'C:/Users/tanyi/Swin-Seg-main/tools/Predict_mask_crop_2017/*.png'
    path3 = 'C:/Users/tanyi/Swin-Seg-main/tools/pred_crop_xmin_2017/*.txt'
    #项目中存放训练所用的npz文件路径
    for i, j, k in zip(glob.glob(path1), glob.glob(path2), glob.glob(path3)):
        pred = cv2.imread(i, flags=0)
        pred_crop = cv2.imread(j, flags=0)
        pred[pred > 128] = 255
        pred[pred <= 128] = 0
        pred_crop[pred_crop > 128] = 255
        pred_crop[pred_crop <= 128] = 0

        bbox = []
        with open(k) as file:
            for item in file:
                item = item.strip('\n')
                bbox.append(item)
        xmin = bbox[0]
        xmax = bbox[1]
        ymin = bbox[2]
        ymax = bbox[3]

        pred[int(ymin):int(ymax), int(xmin):int(xmax)] = pred[int(ymin):int(ymax), int(xmin):int(xmax)] + pred_crop
        #pred[int(ymin):int(ymax), int(xmin):int(xmax)] = image + pred_crop
        #pred[int(ymin):int(ymax), int(xmin):int(xmax)] = pred[int(ymin):int(ymax), int(xmin):int(xmax)] + pred_crop
        #pred[pred != 254] = 0
        #pred[pred == 254] = 1
        pred[pred != 0] = 1

        if not os.path.exists(outpath):
            os.mkdir(outpath)
        #print(i[53:])
        cv2.imwrite(os.path.join(outpath, i[53:]), pred)

    print('ok')

def main():
    merge()

if __name__ == '__main__':
    main()
