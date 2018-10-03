import os
from PIL import Image, ImageEnhance

SRC_DIR = r'/Users/bishnubhusal/Desktop/s-21/image_python'
DEST_DIR = r'/Users/bishnubhusal/Desktop/s-21/brightness'


for file in os.listdir(SRC_DIR):
    full_path = os.path.join(SRC_DIR, file)
    save_full_path = os.path.join(DEST_DIR, file)
    # extension = file.split('.')[-1]
    im = Image.open(full_path)

    bw = im.convert('L')

    bw.show()

    # enh = ImageEnhance.Brightness(im)
    # enh.enhance(1.2).save(save_full_path)