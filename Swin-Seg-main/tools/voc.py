import os
import cv2
from PIL import Image
 
# Make sure the format of your dataset is VOC format
def convert(mask_path):
    cv_img = cv2.imread(mask_path)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGRA2BGR)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2BGRA)
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGRA2RGBA)
    image = Image.fromarray(cv_img).convert(mode="P")
    image.save(mask_path)
 
mask_folder = "data/VOCdevkit/VOC2012/SegmentationClass"
for mask in os.listdir(mask_folder):
    mask_path = os.path.join(mask_folder, mask)
    convert(mask_path)