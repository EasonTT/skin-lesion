import os
import shutil
from sklearn.model_selection import train_test_split

# 创建文件夹
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print(f'-- new folder "{path}" --')
    else:
        print(f'-- the folder "{path}" is already here --')

dataset_path = "C:/Users/tanyi/Swin-Seg-main/tools/data/ade/ISIC2016/images/training"
train_set_save_path = "C:/Users/tanyi/Swin-Seg-main/tools/data/ade/ISIC2016/train"
val_set_save_path = "C:/Users/tanyi/Swin-Seg-main/tools/data/ade/ISIC2016/val"
mkdir(train_set_save_path)
mkdir(val_set_save_path)

file_pathes = os.listdir(dataset_path)
# 获取文件夹下所有 png 格式的图像的名称（不包含后缀名）
img_names = []
for file_path in file_pathes:
    if os.path.splitext(file_path)[1] == ".jpg":
        file_name = os.path.splitext(file_path)[0]
        img_names.append(file_name)

# 划分训练集和验证集
train_set, val_set = train_test_split(img_names, test_size=0.2, random_state=42)
print(f"train_set size: {len(train_set)}, val_set size: {len(val_set)}")

# 训练集处理：将图像和标签文件移动到目标文件夹
for file_name in train_set:
    img_src_path = os.path.join(dataset_path, file_name+".jpg")
    img_dst_path = os.path.join(train_set_save_path, file_name+".jpg")
    shutil.copyfile(img_src_path, img_dst_path)

    img_src_path = os.path.join(dataset_path, file_name + ".png")
    img_dst_path = os.path.join(train_set_save_path, file_name + ".png")
    shutil.copyfile(img_src_path, img_dst_path)

    xml_src_path = os.path.join(dataset_path, file_name+".xml")
    xml_dst_path = os.path.join(train_set_save_path, file_name+".xml")
    shutil.copyfile(xml_src_path, xml_dst_path)

# 验证集处理：将图像和标签文件移动到目标文件夹
for file_name in val_set:
    img_src_path = os.path.join(dataset_path, file_name+".jpg")
    img_dst_path = os.path.join(val_set_save_path, file_name+".jpg")
    shutil.copyfile(img_src_path, img_dst_path)

    img_src_path = os.path.join(dataset_path, file_name + ".png")
    img_dst_path = os.path.join(val_set_save_path, file_name + ".png")
    shutil.copyfile(img_src_path, img_dst_path)

    xml_src_path = os.path.join(dataset_path, file_name+".xml")
    xml_dst_path = os.path.join(val_set_save_path, file_name+".xml")
    shutil.copyfile(xml_src_path, xml_dst_path)
