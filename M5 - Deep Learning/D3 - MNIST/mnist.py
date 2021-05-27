from collections import OrderedDict

import numpy as np
import matplotlib.pyplot as plt
import time

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F

from torchvision import datasets, transforms


# Define a transform to normalize the data (Preprocessing)
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5), (0.5))]
)

# Download and load the training data
trainset = datasets.MNIST("MNIST_data/", download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=16, shuffle=True)

# Download and load the test data
testset = datasets.MNIST("MNIST_data/", download=True, train=False, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=16, shuffle=True)


class Network(nn.Module):

    # Defining the layers, 128, 64, 10 units each
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 10)

    # Forward pass through the network, returns the output logits
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.softmax(x, dim=1)
        return x


model = Network()
print(model)


# Hyperparameters for our network
input_size = 784
hidden_sizes = [4, 4]
output_size = 10

# Build a feed-forward network
model = nn.Sequential(
    nn.Linear(input_size, hidden_sizes[0]),
    nn.ReLU(),
    nn.Linear(hidden_sizes[0], hidden_sizes[1]),
    nn.ReLU(),
    nn.Linear(hidden_sizes[1], output_size),
    nn.Softmax(dim=1),
)
print(model)


model = nn.Sequential(
    OrderedDict(
        [
            ("fc1", nn.Linear(input_size, hidden_sizes[0])),
            ("relu1", nn.ReLU()),
            ("fc2", nn.Linear(hidden_sizes[0], hidden_sizes[1])),
            ("relu2", nn.ReLU()),
            ("output", nn.Linear(hidden_sizes[1], output_size)),
            ("logits", nn.Linear(hidden_sizes[1], output_size)),
            ("softmax", nn.Softmax(dim=1)),
        ]
    )
)
print(model)


# training the network

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
# optimizer = optim.Adam(model.parameters(), lr=0.01)


print("Initial weights - ", model.fc1.weight)

images, labels = next(iter(trainloader))
images.resize_(16, 784)

# Clear the gradients, do this because gradients are accumulated
optimizer.zero_grad()

# Forward pass, then backward pass, then update weights
output = model.forward(images)
loss = criterion(output, labels)
loss.backward()
print("Gradient -", model.fc1.weight.grad)
optimizer.step()


epochs = 3
print_every = 40

for e in range(epochs):
    running_loss = 0
    print(f"Epoch: {e+1}/{epochs}")

    for i, (images, labels) in enumerate(iter(trainloader)):

        # Flatten MNIST images into a 784 long vector
        images.resize_(images.size()[0], 784)

        optimizer.zero_grad()

        output = model.forward(images)  # 1) Forward pass
        loss = criterion(output, labels)  # 2) Compute loss
        loss.backward()  # 3) Backward pass
        optimizer.step()  # 4) Update model

        running_loss += loss.item()

        if i % print_every == 0:
            print(f"\tIteration: {i}\t Loss: {running_loss/print_every:.4f}")
            running_loss = 0
