from collections import OrderedDict

import numpy as np
import matplotlib.pyplot as plt

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


class NNetwork(nn.Module):

    # Defining the layers, 128, 64, 10 units each
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 16)
        self.fc2 = nn.Linear(16, 32)
        self.fc3 = nn.Linear(32, 8)
        self.fc4 = nn.Linear(8, 10)

    # Forward pass through the network, returns the output logits
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.fc4(x)
        return x


model = NNetwork()
# print(model)


# training the network

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
# optimizer = optim.Adam(model.parameters(), lr=0.01)


epochs = 5
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


correct_train = 0
total_train = 0

with torch.no_grad():
    for data in trainset:
        X, y = data
        output1 = model.forward(X.view(-1, 784))
        for idx, i in enumerate(output1):
            if torch.argmax(i) == y[idx]:
                correct_train += 1
            total_train += 1

correct_test = 0
total_test = 0

with torch.no_grad():
    for data in testset:
        X, y = data
        output1 = model.forward(X.view(-1, 784))
        for idx, i in enumerate(output1):
            if torch.argmax(i) == y[idx]:
                correct_test += 1
            total_test += 1

print(f"Accuracy on train set: {round((correct_train/total_train)*100, 3)}%")
print(f"Accuracy on test set: {round((correct_test/total_test)*100, 3)}%")
