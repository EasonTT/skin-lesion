import os

from mmseg.apis import init_segmentor, inference_segmentor, show_result_pyplot
from mmseg.core.evaluation import get_palette
from matplotlib import pyplot as plt
import mmcv
from collections import Counter
from PIL import Image
import numpy as np
from tqdm import tqdm
import cv2

config_file = "../configs/swin/upernet_swin_tiny_patch4_window7_512x512_160k_ade20k.py"
checkpoint_file = "output_diceloss2016/latest.pth"

model = init_segmentor(config_file, checkpoint_file, device='cuda:0')

img_root = "data/ade/test_blurred_lesions/"
save_mask_root = "blurred_mask/"
if not os.path.exists(save_mask_root):
    os.mkdir(save_mask_root)
img_names = os.listdir(img_root)
for img_name in tqdm(img_names):
    # test a single image
    img = img_root + img_name
    result = inference_segmentor(model, img)[0]
    img = Image.fromarray(np.uint8(result*255))
    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    opencvImage = cv2.cvtColor(opencvImage, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(save_mask_root, img_name[:-4]+'.png'), opencvImage)
    #img.save(save_mask_root + img_name)
