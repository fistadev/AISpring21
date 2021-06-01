import data_handler as dh
from rnn import Model
from torch.optim import Adam, SGD
from torchsummary import summary
from torch.autograd import Variable
from torch import nn
import torch
import matplotlib.pyplot as plt

x_train = dh.df_train
x_test = dh.df_test

n_steps = 40
n_inputs = 7
n_neurons = 100
hidden_dim = n_steps
n_outputs = 1
learning_rate = 0.01
batch_size = 50

LSTM = Model(n_inputs, n_neurons, hidden_dim)

# LSTM.cuda()

optim = Adam(LSTM.parameters(), lr=learning_rate)

criterion = nn.L1Loss()


def train(n_iterations, data):
    best_val = 1000
    train_loss = []
    for iter in range(n_iterations):

        x_batch, y_batch = dh.next_stock_batch(batch_size, hidden_dim, data)
        x_batch, y_batch = torch.from_numpy(x_batch), torch.from_numpy(y_batch).squeeze(-1)
        x_batch, y_batch = Variable(x_batch).float(), Variable(y_batch).float()

        # x_batch.cuda()
        # y_batch.cuda()
        # print(x_batch.shape)
        # print(y_batch.size)

        optim.zero_grad()
        outputs = LSTM(x_batch)

        # print(outputs.shape)
        # print(y_batch.shape)

        loss = criterion(y_batch.flatten(), outputs)
        loss.backward()
        # print(loss)
        optim.step()
        train_loss.append(loss.item())
        if iter % 50 == 0:

            x_batch, y_batch = dh.next_stock_batch(batch_size, n_steps, x_test)
            x_batch, y_batch = torch.from_numpy(x_batch), torch.from_numpy(y_batch).squeeze(-1)
            x_batch, y_batch = Variable(x_batch).float(), Variable(y_batch).float()

            with torch.no_grad():
                outputs = LSTM(x_batch)
                test_loss = criterion(y_batch.flatten(), outputs)

            if best_val > test_loss:
                best_val = test_loss
                torch.save(LSTM, "Best_val_model.pth")
            print(iter, "\t Train Loss:", loss.item(), "\t Test Loss:", test_loss.item())

    plt.plot(train_loss, label="Train Loss")
    plt.xlabel(" Iteration ")
    plt.ylabel("Loss value")
    plt.legend(loc="upper left")
    plt.show()


train(501, x_train)
LSTM = torch.load("model2.pth")

x_batch, y_batch = dh.next_stock_batch(batch_size, n_steps, x_train)
x_batch, y_batch = torch.from_numpy(x_batch), torch.from_numpy(y_batch).squeeze(-1)
x_batch, y_batch = Variable(x_batch).float(), Variable(y_batch).float()

# if torch.cuda.is_available():
#     x_batch.cuda()
#     y_batch.cuda()

with torch.no_grad():
    outputs = LSTM(x_batch)
    loss = criterion(y_batch.flatten(), outputs)
    print(loss)

y = y_batch.cpu().numpy().reshape((batch_size, hidden_dim))[0, :]
o = outputs.cpu().numpy().reshape((batch_size, hidden_dim))[0, :]

plt.plot(y, label="Ground truth")
plt.plot(o, label="Prediction")
plt.xlabel(" Time ")
plt.ylabel("Stock return")
plt.legend(loc="upper left")
plt.show()

x_batch, y_batch = dh.next_stock_batch(batch_size, n_steps, x_test)
x_batch, y_batch = torch.from_numpy(x_batch), torch.from_numpy(y_batch).squeeze(-1)
x_batch, y_batch = Variable(x_batch).float(), Variable(y_batch).float()

# if torch.cuda.is_available():
#     x_batch.cuda()
#     y_batch.cuda()

with torch.no_grad():
    outputs = LSTM(x_batch)
    loss = criterion(y_batch.flatten(), outputs)
    print(loss)

y = y_batch.cpu().numpy().reshape((batch_size, hidden_dim))[0, :]
o = outputs.cpu().numpy().reshape((batch_size, hidden_dim))[0, :]

# print(o)
# print(y)
print(outputs.shape)
plt.plot(y, label="Ground truth")
plt.plot(o, label="Prediction")
plt.xlabel(" Time ")
plt.ylabel("Stock return")
plt.legend(loc="upper left")
plt.show()