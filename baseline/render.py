from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
import open3d as o3d
from PIL import Image
import numpy as np 
import cv2 

import trimesh
import pyrender
import numpy as np

tm = trimesh.load('CAD_model/whole_mm_2.STL') 
mesh = pyrender.Mesh.from_trimesh(tm)

#tx, ty, tz, rx, ry, rz = (0.0, 0.0, -200.0, -179.999985, 2.38308, -179.999985) #DATASET 1 / 0 ok
#tx, ty, tz, rx, ry, rz = (50.0, 0.0, -200.0, -179.999985, -14.80563, -179.999985) #DATASET 1 / 1 ok
#tx, ty, tz, rx, ry, rz = (0.0, -50.0, -200.0, -179.999985, 8.112659, -179.999985) #DATASET 1 / 2 ok
#tx, ty, tz, rx, ry, rz = (0.0, 0.0, -200.0, 151.352127, 8.112659, -179.999985) #DATASET 1 / 3 ok
#tx, ty, tz, rx, ry, rz = (0.0, 0.0, -200.0, -179.999985, 2.383087, 174.270416) #DATASET 1 / 5 ok
#tx, ty, tz, rx, ry, rz = (0.0, 0.0, -200.0, 168.540802, -20.535173, -179.999985) #DATASET 1 / 8 ok
#tx, ty, tz, rx, ry, rz = (0.0, 0.0, -200.0, 157.081741, 2.383087, 168.540802) #DATASET 1 / 9 ok
#tx, ty, tz, rx, ry, rz = (-50.0, 50.0, -200.0, 162.811218, 8.112659, 157.081741) #DATASET 1 / 10 ok
#tx, ty, tz, rx, ry, rz = (-50.0, -50.0, -200.0, -179.999969, 0.0, -179.999969) #DATASET 3 / 3 ok
#tx, ty, tz, rx, ry, rz = (-50.0, 50.0, -200.0, 162.811218, -14.80563, -157.081741) #DATASET 2 / 1 ok
#tx, ty, tz, rx, ry, rz = (50.0, -50.0, -200.0, 162.811203, 13.842224, 157.081741) #DATASET 2 / 2 ok
#tx, ty, tz, rx, ry, rz = (-50.0, -50.0, -200.0, -162.811203, -3.346499, 151.352127) #DATASET 2 / 3 ok
tx, ty, tz, rx, ry, rz = (49.0, -21.0, -295.0, -180.0, 6.20606, 100.512138)


r = R.from_euler('xyz',[rx, ry, rz], degrees=True)
#r = R.from_euler('zyx',[rx, ry, rz], degrees=True)

Twc = np.eye(4)
Twc[:3,:3] = r.as_matrix()
Twc[:3,3] = np.array([tx, ty, tz])

Twc [0,1] *= -1
Twc [1,0] *= -1
Twc [1,2] *= -1
Twc [2,1] *= -1

Twc [0,3] *= -1

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
color = color[::-1,:,:]
depth = depth[::-1,:]

# Flip x in image space
color = color[:,::-1,:]
depth = depth[:,::-1]

print(depth.shape)

cv2.imwrite('out.png', color)

# Overlap the two images for comparision
fig = plt.figure()
img = Image.open("DATASET_5/5-U_.png")
img1 = Image.open("DATASET_5/5-N_.png")
#plt.imshow(img, alpha=0.6, cmap=plt.cm.gray)
#plt.imshow(img1, alpha=0.4, cmap=plt.cm.gray)
plt.imshow(depth, alpha=0.3, cmap=plt.cm.gray_r)
#plt.gca().invert_xaxis()
plt.show()