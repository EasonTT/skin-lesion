import os

def main():
    #img_dir = 'C:/Users/Chadm/chainer-skin-lesion-detector/data/ISIC2018_Task1-2_Validation_Input/'
    gt_dir = 'C:/Users/tanyi/Swin-Seg-main/tools/data/ade/ISIC2017/annotations/test/'
    name_list = os.listdir(gt_dir)
    for i, name in enumerate(name_list):
        #os.rename(img_dir + name, img_dir + str(i) + '.jpg')
        os.rename(gt_dir + name, gt_dir + name[:-17] + '.png')


if __name__ == "__main__":
    main()