import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd

# class CustomDataset(Dataset):
#     def __init__(self):
#         pass
#     def _getitem__(self, index):
#         pass

PATH = 'https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv'
df = pd.read_csv(PATH)
columns = ['Living', 'Rooms', 'Beds', 'Baths', 'Age', 'Acres', 'Taxes']
df.columns = [x.replace('"', "").replace(" ", "") for x in df.columns]

print(df.head())
print('*********************************************')
print('Above 152k: ', (df.Sell.values > 152).sum())
print('Below 152k: ', (df.Sell.values <= 152).sum())
print('*********************************************')

# trial = CustomDataset()

# trial = [1,2,3,4,5,6]
# print(trial[2])
#
# print(trial.__len__())

class HouseDataset(Dataset):
    def __init__(self, PATH, budget=152):
        df = pd.read_csv(PATH)
        df.columns = [x.replace('"', "").replace(" ", "") for x in df.columns]
        columns = ['Living', 'Rooms', 'Beds', 'Baths', 'Age', 'Acres', 'Taxes']
        self.features = df[columns].values
        self.labels = (df.Sell.values <= budget).astype('int')
        self.n_samples = len(self.features)
    def _getitem__(self, index):
        return self.features[index], self.labels[index]
    def __len__(self):
        return self.n_samples

print('*********************************************')

trial = HouseDataset(PATH, budget=152)
# x, y = trial[3]
# print(len(trial))
# print(x)
# print(y)
print('*********************************************')

trial_loader = DataLoader(dataset=trial, batch_size=3, shuffle=True)
print(trial_loader)
print('*********************************************')

data_iter = iter(trial_loader)
print(data_iter.next())
print('*********************************************')

# print('Above 152k: ', (df.Sell.values > 152).sum())
# print('Below 152k: ', (df.Sell.values <= 152).sum())

