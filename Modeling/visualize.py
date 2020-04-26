import matplotlib.pyplot as plt
from celluloid import Camera
import torch
from baseline import *
from modules import *
import numpy as np

def gen_gif(data1, data2):
    fig = plt.figure()
    camera = Camera(fig)
    for i in range(len(data1)):
        plt.ioff()
        plt.subplot(1, 2, 1)
        plt.imshow(data1[i].permute(1, 2, 0))
        plt.title("Original")
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(data2[i].permute(1, 2, 0))
        plt.title("Reconstructed")
        plt.axis('off')
        camera.snap()
    return camera.animate()


device = 'cpu'
model = torch.load("./model.pth").to(device)

# Load in data, forward pass it, and create gif

import os
data_folder = '../data/'
files = os.listdir(data_folder)

for file in files:
    # Parse out batch number
    batch_num = file.split('_')[-1].split('.')[0]
    print("Visualizing batch %s" % (batch_num))
    
    # Load in the data
    x = torch.as_tensor(np.load(os.path.join(data_folder, file))).float().to(device).permute(0, 3, 1, 2)
    
    # Forward pass baby! [throw away encoding]
    with torch.no_grad():
        y, _ = model(x)
        # Threshold
        y[y>1] = 1
    
    gif = gen_gif(x.cpu(), y.cpu())
    gif.save("batch_%s.gif" % batch_num)
    
    del x, y, gif
    

