import baseline as b
#import capture_data as d
#import visualize as v
import torch
import numpy as np

#Declare model
model = b.Baseline('cuda:0').to('cuda:0')

#Load in data
data = torch.as_tensor(np.load('../data/batch_0.npz')).float().to('cuda').permute(0, 3, 1, 2)

# checkpoint = torch.load('checkpoint.pth')
#checkpoint = torch.load('checkpoint.pth')

# model.do_train_on_vid('training_data/vid1', 100000, batch_size=4, checkpoint=checkpoint)
#model.do_train_on_vid('training_data/vid1', 100000, batch_size=8, checkpoint=checkpoint)
model.do_train(data, data, 1000, batch_size=8)


