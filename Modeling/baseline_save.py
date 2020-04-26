import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim
import matplotlib.pyplot as plt
import modules as m


class Baseline(nn.Module):
    def __init__(self, device):
        super(Baseline, self).__init__()

        self.device = device

        self.conv1 = m.CNNBlock2d(3, 4, 3, use_wavelet=True)
        self.conv2 = m.CNNBlock2d(4, 16, 3)
        self.conv3 = m.CNNBlock2d(16, 32, 3)

        self.deconv2 = m.TransposedCNNBlock2d(32, 16, 4)
        self.deconv3 = m.TransposedCNNBlock2d(16, 4, 4)
        self.deconv4 = m.TransposedCNNBlock2d(5, 3, 4)

    def forward(self, x):
        plt.imsave("./frames_m1/input.jpg", x.cpu().squeeze().permute(1, 2, 0).numpy())
        interm_out, res = self.conv1(x)
        plt.imsave("./frames_m1/res.jpg", res.squeeze().cpu().detach().numpy(), cmap="grayscale")

        plt.imsave("./frames_m1/l1.jpg", (
            torch.cat((torch.max(interm_out[:, :2], 1).values.unsqueeze(1), interm_out[:, 2:]),
                      1)).cpu().squeeze().permute(1, 2, 0).detach().numpy() / interm_out.max().cpu().detach().numpy())
        interm_out = self.conv2(interm_out)
        plt.imsave("./frames_m1/l2.jpg", (torch.cat(
            (
                torch.max(interm_out[:, :5], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 5:10], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 10:15], 1).values.unsqueeze(1)
            ), 1)).cpu().squeeze().permute(1, 2, 0).detach().numpy() / interm_out.max().cpu().detach().numpy())

        interm_out = self.conv3(interm_out)
        plt.imsave("./frames_m1/l3.jpg", (torch.cat(
            (
                torch.max(interm_out[:, :10], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 10:20], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 20:30], 1).values.unsqueeze(1)
            ), 1)).cpu().squeeze().permute(1, 2, 0).detach().numpy() / interm_out.max().cpu().detach().numpy())

        plt.imsave("./frames_m1/l3.jpg", (torch.cat(
            (
                torch.max(interm_out[:, :10], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 10:20], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 20:30], 1).values.unsqueeze(1)
            ), 1)).cpu().squeeze().permute(1, 2, 0).detach().numpy() / interm_out.max().cpu().detach().numpy())
        interm_out = self.deconv2(interm_out)
        plt.imsave("./frames_m1/l4.jpg", (torch.cat(
            (
                torch.max(interm_out[:, :5], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 5:10], 1).values.unsqueeze(1),
                torch.max(interm_out[:, 10:15], 1).values.unsqueeze(1)
            ), 1)).cpu().squeeze().permute(1, 2, 0).detach().numpy() / interm_out.max().cpu().detach().numpy())
        interm_out = self.deconv3(interm_out)
        plt.imsave("./frames_m1/l5.jpg", (
            torch.cat(
                (
                    torch.max(interm_out[:, :2], 1).values.unsqueeze(1),
                    interm_out[:, 2:]
                ),
                1)).cpu().squeeze().permute(1, 2, 0).detach().numpy() / interm_out.max().cpu().detach().numpy())

        interm_out = torch.cat((interm_out, res), 1)
        interm_out = self.deconv4(interm_out)
        plt.imsave("./frames_m1/l6.jpg", interm_out.cpu().squeeze().permute(1, 2,
                                                                            0).detach().numpy() / interm_out.max().cpu().detach().numpy())

    def encode(self, x):
        interm_out, res = self.conv1(x)
        interm_out = self.conv2(interm_out)
        interm_out = self.conv3(interm_out)

        return interm_out

    def do_train(self, x, y, epochs, batch_size=128, lr=1e-3, verbose=1, checkpoint=None):
        optimizer = optim.Adam(self.parameters(), lr=lr)
        scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer)

        if checkpoint:
            self.load_state_dict(checkpoint['state_dict'])
            self.to(self.device)
            optimizer.load_state_dict(checkpoint['optimizer'])
            for state in optimizer.state.values():
                for k, v in state.items():
                    if isinstance(v, torch.Tensor):
                        state[k] = v.to(self.device)
        min_loss = 1e8
        for epoch in range(epochs):
            # self.train()
            # Shuffle data for stochastic iteration
            shuffle = np.random.permutation(len(x))
            x = x[shuffle]
            y = y[shuffle]
            # Interate through data
            running_loss = 0

            for batch_idx in range(len(x) // batch_size):
                xbatch = x[batch_idx * batch_size:(batch_idx + 1) * batch_size].to(self.device).float()
                ybatch = y[batch_idx * batch_size:(batch_idx + 1) * batch_size].to(self.device).float()

                y_hat, encoding = self.forward(xbatch)

                loss = ((y_hat - ybatch) ** 2).mean()

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                # if not torch.isnan(loss):
                running_loss += loss.detach()

            running_loss /= (len(x) // batch_size)

            if (epoch + 1) % verbose == 0:
                print('[%d]: %.16f' % (epoch + 1, running_loss))
                scheduler.step(running_loss)
                if running_loss < min_loss:
                    min_loss = running_loss
                    # Save network
                    checkpoint = {'state_dict': self.state_dict(),
                                  'optimizer': optimizer.state_dict()}

                    torch.save(checkpoint, 'checkpoint.pth')
                    torch.save(self, 'model.pth')

    def do_train_on_vid(self, folder_path, epochs, batches_per_epoch=25, batch_size=64, lr=1e-5, lambda_coef=1e-3,
                        verbose=1, checkpoint=None):
        import os
        optimizer = optim.Adam(self.parameters(), lr=lr)
        scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer)

        if checkpoint:
            self.load_state_dict(checkpoint['state_dict'])
            self.to(self.device)
            optimizer.load_state_dict(checkpoint['optimizer'])
            for state in optimizer.state.values():
                for k, v in state.items():
                    if isinstance(v, torch.Tensor):
                        state[k] = v.to(self.device)

        min_loss = 1e8
        count = 0
        test_frame = torch.load(os.path.join(folder_path, 'frame0'))

        for epoch in range(epochs):
            count = 0
            running_loss = 0

            for batch_idx in range(batches_per_epoch):

                xbatch = torch.zeros(batch_size, test_frame.shape[1], test_frame.shape[2], test_frame.shape[3])
                ybatch = torch.zeros(batch_size, test_frame.shape[1], test_frame.shape[2], test_frame.shape[3])

                # March through the data
                for i in range(batch_size):
                    img = torch.load(os.path.join(folder_path, 'frame' + str(count)))
                    xbatch[i] = img
                    ybatch[i] = img

                xbatch = xbatch.to(self.device)
                ybatch = ybatch.to(self.device)

                y_hat, encoding = self.forward(xbatch)

                L1_loss = lambda_coef * torch.abs(encoding).mean()
                loss = ((y_hat - ybatch) ** 2).mean() + L1_loss

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                # if not torch.isnan(loss):
                running_loss += loss.detach()

            running_loss /= batches_per_epoch

            if (epoch + 1) % verbose == 0:
                print('[%d]: %.16f %.8f' % (epoch + 1, running_loss, L1_loss))
                scheduler.step(running_loss)
                if running_loss < min_loss:
                    min_loss = running_loss
                    # Save network
                    checkpoint = {'state_dict': self.state_dict(),
                                  'optimizer': optimizer.state_dict()}

                    torch.save(checkpoint, 'checkpoint.pth')
                    torch.save(self, 'model.pth')


def sparsify(x):
    idx = torch.nonzero(x, as_tuple=True)
    data = x[idx]

    return data, idx, data.shape


def de_sparsify(x, idx, shape):
    out = torch.zeros(shape)
    out[idx] = x

    return out




