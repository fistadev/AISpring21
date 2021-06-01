from typing import Tuple
import torch
from torch import nn
from torch.nn.modules import dropout
from torch.nn.modules.linear import Linear
from torch.autograd import Variable


class Model(nn.Module):

    def __init__(self, input_size, neurons, hidden_size):
        super(Model, self).__init__()

        self.neurons = neurons
        self.hidden_size = hidden_size

        self.rnn = nn.LSTM(input_size, self.hidden_size, neurons, batch_first=True, dropout=0)

        self.linear1 = Linear(50 * hidden_size, 50 * hidden_size)

        self.relu = nn.ReLU()

    def forward(self, x):
        h0 = Variable(torch.zeros(self.neurons, x.shape[0], self.hidden_size))
        c0 = Variable(torch.zeros(self.neurons, x.shape[0], self.hidden_size))

        out, (hn, cn) = self.rnn(x.cuda(), (h0.cuda(), c0.cuda()))
        hn = hn[-1]

        out = self.relu(hn.flatten())
        out = self.linear1(out)

        return out