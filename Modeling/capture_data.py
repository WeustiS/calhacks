import cv2
import numpy as np
import torch

def get_frames(filepath, max_frames=1e7, verbose=1000):
    

    vidcap = cv2.VideoCapture(filepath)
    success,image = vidcap.read()
    count = 0

    data = []

    while success and count < max_frames:
        # save frame as JPEG file      
        success, image = vidcap.read()
        data.append(image / 255)
        count += 1
        if verbose != -1 and count%verbose==0:
            print("Loading video %s: %.2f%%" % (filepath, count * 100 / max_frames))


    data = np.array(data)
    data = torch.as_tensor(data)
    return data.permute(0, 3, 1, 2)

def decompose(file_path, save_path, batch_size=64):
    import os
    vidcap = cv2.VideoCapture(file_path)
    success,preimage = vidcap.read()
    count = 0
    fake_count = 0
    
    while success:
        # save frame as JPEG file      
        success = vidcap.grab()
        
        if count%20==0 and count > 60000:
            success,image = vidcap.read()
            image = torch.from_numpy(np.transpose((image / 255), (2, 0, 1))).unsqueeze(0)
            torch.save(image, os.path.join(save_path, 'frame' + str(fake_count)))
            fake_count += 1
            print(fake_count)
        count += 1













