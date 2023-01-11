import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
import os
from MyNet import MyNet

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, ), (0.5, )),
])
mnist_trainset = datasets.MNIST(root='./data',
                                train=True,
                                download=True,
                                transform=transform)

train_loader = torch.utils.data.DataLoader(mnist_trainset,
                                           batch_size=10,
                                           shuffle=True)

mnist_testset = datasets.MNIST(root='./data',
                               train=False,
                               download=True,
                               transform=transform)
test_loader = torch.utils.data.DataLoader(mnist_testset,
                                          batch_size=10,
                                          shuffle=True)

net = MyNet()

cross_el = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)  #e-1
epoch = 10

for epoch in range(epoch):
    net.train()

    for data in test_loader:
        x, y = data
        optimizer.zero_grad()
        output = net(x.view(-1, 28 * 28))
        loss = cross_el(output, y)
        loss.backward()
        optimizer.step()

correct = 0
total = 0

with torch.no_grad():
    for data in train_loader:
        x, y = data
        output = net(x.view(-1, 784))
        for idx, i in enumerate(output):
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1
print(f'accuracy: {round(correct/total, 3)}')

#visualization
plt.imshow(x[3].view(28, 28))
plt.show()
print(torch.argmax(net(x[3].view(-1, 784))[0]))
