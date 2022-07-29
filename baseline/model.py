# torch
import torch
from torch.nn import Conv2d, MaxPool2d
import torch.nn as nn
import torch.nn.functional as F

# define Resnet building blocks
class ResidualBlock(nn.Module):
    def __init__(self, inchannel, outchannel, stride=1):
        super(ResidualBlock, self).__init__()
        self.left = nn.Sequential(Conv2d(inchannel, outchannel, kernel_size=3,
                                         stride=stride, padding=1, bias=False),
                                  nn.BatchNorm2d(outchannel),
                                  nn.ReLU(inplace=True),
                                  Conv2d(outchannel, outchannel, kernel_size=3,
                                         stride=1, padding=1, bias=False),
                                  nn.BatchNorm2d(outchannel))
        self.shortcut = nn.Sequential()

        if stride != 1 or inchannel != outchannel:
            self.shortcut = nn.Sequential(Conv2d(inchannel, outchannel,
                                                 kernel_size=1, stride=stride,
                                                 padding=0, bias=False),
                                          nn.BatchNorm2d(outchannel))

    def forward(self, x):
        out = self.left(x)
        out += self.shortcut(x)
        out = F.relu(out)
        return out

# define Resnet
class ResNet(nn.Module):
    def __init__(self, ResidualBlock, num_classes=6):
        super(ResNet, self).__init__()

        self.inchannel = 64
        self.conv1 = nn.Sequential(Conv2d(3, 64, kernel_size = 7, stride = 2, padding = 3, bias = False), 
                                  nn.BatchNorm2d(64), 
                                  nn.ReLU())
        self.maxpool = nn.MaxPool2d(2, stride=2, padding=1)
        self.layer1 = self.make_layer(ResidualBlock, 64, 2, stride = 2)
        self.maxpool2 = nn.MaxPool2d(2, stride=1, padding=1)
        self.layer2 = self.make_layer(ResidualBlock, 128, 2, stride = 2)
        self.layer3 = self.make_layer(ResidualBlock, 256, 2, stride = 2)
        self.layer4 = self.make_layer(ResidualBlock, 512, 2, stride = 2)
        self.layer5 = self.make_layer(ResidualBlock, 256, 2, stride = 2)
        self.avgpool = nn.AvgPool2d(4)
        self.fc = nn.Linear(512, num_classes)

    def make_layer(self, block, channels, num_blocks, stride):
        strides = [stride] + [1] * (num_blocks - 1)
        layers = []
        for stride in strides:
            layers.append(block(self.inchannel, channels, stride))
            self.inchannel = channels
        return nn.Sequential(*layers)

    def forward(self, x):
        #print('x_shape', x.shape)
        x = self.conv1(x)
        #print('x_shape', x.shape)
        x = self.maxpool(x)
        #print('x_shape', x.shape)
        x = self.layer1(x)
        #print('x_shape', x.shape)
        x = self.maxpool2(x)
        #print('x_shape', x.shape)
        x = self.layer2(x)
        #print('x_shape', x.shape)
        x = self.maxpool2(x)
        #print('x_shape', x.shape)
        x = self.layer3(x)
        #print('x_shape', x.shape)
        x = self.maxpool2(x)
        #print('x_shape', x.shape)
        x = self.layer4(x)
        #print('x_shape', x.shape)
        #x = self.maxpool2(x)
        #print('x_shape', x.shape)
        #x = self.layer4(x)
        #print('x_shape', x.shape)
        x = self.avgpool(x)
        #print('x_shape', x.shape)
        x = x.view(x.size(0), -1)
        #print('x_shape', x.shape)
        x = self.fc(x)
        #print('x_shape', x.shape)
        return x

