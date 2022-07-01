from PIL import Image
from glob import glob
from os import path

directory = 'C:\Users\39331\Documents\Final Year Project\surfemb\data\THALES\images'

images = [Image.open(jpg) for jpg in glob(path.join(directory, '*-N_.jpg'))]

print(images)
