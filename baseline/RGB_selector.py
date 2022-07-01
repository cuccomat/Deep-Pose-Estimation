import shutil
import os

dataset_paths = []
path = r"C:/Users/39331\Documents/Final Year Project/surfemb/data/THALES/images"
dest_path = r'C:/Users/39331/Documents/Final Year Project/surfemb/data/THALES/RGB_images'

for file in os.listdir(path):
    if '-N_.png' in file:
        dataset_paths.append(os.path.join(path,file))
        shutil.copyfile(os.path.join(path,file), os.path.join(dest_path,file))

#for src in dataset_paths:
#    shutil.copyfile(src, r'C:/Users/39331/Documents/Final Year Project/surfemb/data/THALES/RGB_images')