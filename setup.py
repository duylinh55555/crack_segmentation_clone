# import subprocess
# subprocess.call(['sh', 'setup.py'])

import os

os.system("sudo apt install git-all")
os.system("gdown https://drive.google.com/uc?id=1xrOqv0-3uMHjZyEUrerOYiYXW_E8SUMP")
os.system("mkdir ./models")
os.system("gdown https://drive.google.com/uc?id=1wA2eAsyFZArG3Zc9OaKvnBuxSAPyDl08 -O ""./models/model_unet_vgg_16_best.pt""")
# os.system("")