import torch
import torch.nn as nn
import torch.nn.functional as F

import pywt

class CNNBlock2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, down_sample=2, use_batch_norm=True, use_CReLU=False, use_wavelet=False):
        super(CNNBlock2d, self).__init__()
        #Cast to global variables
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.down_sample=down_sample
        self.use_batch_norm = use_batch_norm
        self.use_CReLU = use_CReLU
        self.use_wavelet = use_wavelet
        
        #Define ConvLayer
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, padding=int((kernel_size-1)/2))
        
        if use_batch_norm:
            self.batch_norm = nn.BatchNorm2d(out_channels)
        
        if down_sample != 1:
            self.pooling = nn.MaxPool2d(down_sample, stride=down_sample)
            
        if down_sample == 2 and use_wavelet:
            #Generate wavelet coefs
            w = pywt.Wavelet('db1')

            dec_hi = torch.tensor(w.dec_hi[::-1]) 
            dec_lo = torch.tensor(w.dec_lo[::-1])
            rec_hi = torch.tensor(w.rec_hi)
            rec_lo = torch.tensor(w.rec_lo)
            
            filters = torch.stack([dec_lo.unsqueeze(0)*dec_lo.unsqueeze(1),
                                   dec_lo.unsqueeze(0)*dec_hi.unsqueeze(1),
                                   dec_hi.unsqueeze(0)*dec_lo.unsqueeze(1),
                                   dec_hi.unsqueeze(0)*dec_hi.unsqueeze(1)], dim=0)
            filters = filters.expand([in_channels] + list(filters.shape)).permute(1, 0, 2, 3)
    
            self.wave_filt = torch.nn.Parameter(filters)
            self.wave_filt.requires_grad= False
            
        
    def forward(self, x, thresh=0.1):
        
        if self.use_wavelet:
            res = torch.nn.functional.conv2d(x, self.wave_filt, stride=2)
            res = torch.max(res[:,1:], dim=1).values.unsqueeze(1)
            res = torch.nn.functional.relu(res - thresh)

        interm_out = self.conv(x)
        if self.use_batch_norm:
            interm_out = self.batch_norm(interm_out)
        if self.down_sample != 1:
            interm_out = self.pooling(interm_out)
        #Apply activation
        if self.use_CReLU:
            interm_out = torch.cat((F.relu(interm_out), F.relu(-interm_out)), 1)
        else:
            interm_out = F.relu(interm_out)
        
        if self.use_wavelet:
            return interm_out, res
        else:
            return interm_out

class TransposedCNNBlock2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, up_sample=2, use_batch_norm=False):
        super(TransposedCNNBlock2d, self).__init__()
        #Cast to global variables
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.up_sample=up_sample
        self.use_batch_norm = use_batch_norm
        
        #Define transposed convolution
        self.deconv = nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride=up_sample, padding=int((kernel_size-up_sample)/2))
        
        if use_batch_norm:
            self.batch_norm = nn.BatchNorm2d(out_channels)
        
    def forward(self, x):
        interm_out = self.deconv(x)
        if self.use_batch_norm:
            interm_out = self.batch_norm(interm_out)
        interm_out = F.relu(interm_out)
        return interm_out
