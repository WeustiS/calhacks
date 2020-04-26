import numpy as np
import matplotlib.pyplot as plt
import torch

import pywt
import pywt.data


# Load image
original = plt.imread('test.jpg')[:,:896,:]

# Take one channel for now
img = torch.as_tensor(original[:,:,:]).permute(2, 0, 1)[None,...].float() / 255

#Get filters
w=pywt.Wavelet('db1')

dec_hi = torch.tensor(w.dec_hi[::-1]) 
dec_lo = torch.tensor(w.dec_lo[::-1])
rec_hi = torch.tensor(w.rec_hi)
rec_lo = torch.tensor(w.rec_lo)

filters = torch.stack([dec_lo.unsqueeze(0)*dec_lo.unsqueeze(1),
                       dec_lo.unsqueeze(0)*dec_hi.unsqueeze(1),
                       dec_hi.unsqueeze(0)*dec_lo.unsqueeze(1),
                       dec_hi.unsqueeze(0)*dec_hi.unsqueeze(1)], dim=0)

inv_filters = torch.stack([rec_lo.unsqueeze(0)*rec_lo.unsqueeze(1),
                           rec_lo.unsqueeze(0)*rec_hi.unsqueeze(1),
                           rec_hi.unsqueeze(0)*rec_lo.unsqueeze(1),
                           rec_hi.unsqueeze(0)*rec_hi.unsqueeze(1)], dim=0)

def wt(vimg, levels=1):
    h = vimg.size(2)
    w = vimg.size(3)
    #padded = torch.nn.functional.pad(vimg,(1,1))
    padded=vimg
    print(padded.shape)
    channels = vimg.shape[1]
    res = torch.nn.functional.conv2d(padded, filters.expand([channels] + list(filters.shape)).permute(1, 0, 2, 3), stride=2)
    #if levels>1:
    #    res[:,:1] = wt(res[:,:1],levels-1)
    #res = res.view(-1,2,h//2,w//2).transpose(1,2).contiguous().view(-1,1,h,w)
    return res

def percent_zeros(x, thresh=0):
    return len(x[x<=thresh])/len(x.reshape(-1))
