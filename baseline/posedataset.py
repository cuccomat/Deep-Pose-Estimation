# torch
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

import pandas as pd
import numpy as np
import os 
import imageio


class PoseDataset(Dataset):

    def __init__(self, csv_file, root_dir):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        poses = pd.read_csv(csv_file)
        self.poses = poses.sort_values(by=["id"])
        self.root_dir = root_dir
    

    def __len__(self):
        return len(self.poses)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_path = os.path.join(self.root_dir,
                                str(self.poses.iloc[idx, 0]) + '-N_.png')
        
        img = imageio.imread(img_path, ignoregamma = True)
        rgb_img = img[:,:,:3]
        img_tensor = torch.tensor(rgb_img)/255.0
        img_tensor = np.transpose(img_tensor, (2, 0, 1))
        
        img_downsampled = F.interpolate(img_tensor, scale_factor = 0.25)
        img_downsampled = np.transpose(img_downsampled, (0, 2, 1))
        img_downsampled = F.interpolate(img_downsampled, scale_factor = 0.25)
        img_downsampled = np.transpose(img_downsampled, (0, 2, 1))

        pose = self.poses.iloc[idx, 1:]
        pose = np.array([pose])
        pose =  pose.reshape(6)      
        return img_downsampled, pose