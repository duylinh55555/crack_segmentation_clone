# import subprocess
# subprocess.call(['sh', 'setup.py'])

import os
import zipfile

os.system("sudo apt install git-all")
os.system("gdown https://drive.google.com/uc?id=1xrOqv0-3uMHjZyEUrerOYiYXW_E8SUMP")
os.system("mkdir ./models")
os.system("gdown https://drive.google.com/uc?id=1wA2eAsyFZArG3Zc9OaKvnBuxSAPyDl08 -O ""./models/model_unet_vgg_16_best.pt""")
# os.system("")

extract_folder_path = "img_data"
path = "crack_segmentation_dataset.zip"

with zipfile.ZipFile(path, 'r') as zip_file:
    zip_file.extractall(extract_folder_path)