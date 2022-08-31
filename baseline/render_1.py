from scipy.spatial.transform import Rotation as R
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import cv2 

import trimesh
import pyrender
import numpy as np

tm = trimesh.load('CAD_model/small sat.STL')
mesh = pyrender.Mesh.from_trimesh(tm)

tx, ty, tz, rx, ry, rz = (-53.0, 35.0, -280.0, 180.0, 19.995985, 176.320374)

ty = -ty
ry = -ry 
rz = -rz 

r = R.from_euler('xyz',[rx, ry, rz], degrees=True)

Twc = np.eye(4)
Twc[:3,:3] = r.as_matrix()
Twc[:3,3] = np.array([tx, ty, tz])

print('Twc', Twc)

im_width, im_height = (1024,1024)
camK = np.array([[886.81,0.0,512.0],[0.0,886.81,512.0],[0.0,0.0,1.0]])

camera = pyrender.IntrinsicsCamera(camK[0,0],camK[1,1],
                                    camK[0,2],camK[1,2], zfar = 400.0)
scene=pyrender.Scene()
scene.add(camera,pose=Twc)
scene.add(mesh,pose=np.eye(4))

r = pyrender.OffscreenRenderer(im_width, im_height)
color,depth = r.render(scene)


# Flip y in image space
color = color[:,:,:]
depth = depth[:,:]

print(depth.shape)

cv2.imwrite('out_1.png', color)
img = Image.open("RGB_images_equatoriale/0-N_.png")
# Overlap the two images for comparision
fig = plt.figure()

#img1 = Image.open("DATASET_5/5-N_.png")
plt.imshow(img, alpha=0.6, cmap=plt.cm.gray)
plt.show()
#plt.imshow(img1, alpha=0.4, cmap=plt.cm.gray)
fig = plt.figure()
plt.imshow(depth, alpha=0.5, cmap=plt.cm.gray)
#plt.gca().invert_xaxis()
plt.show()
