import shutil
import os

dataset_paths = []
path = r"C:/Users/39331\Documents/Final Year Project/surfemb/data/THALES/images"
dest_path = r'C:/Users/39331/Documents/Final Year Project/baseline/poses'

for file in os.listdir(path):
    if '.txt' in file:
        dataset_paths.append(os.path.join(path,file))
        shutil.copyfile(os.path.join(path,file), os.path.join(dest_path,file))
