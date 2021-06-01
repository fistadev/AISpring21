import numpy as np
import pandas as pd

df = pd.read_csv("data_akbilgic.csv")

df_train = df[:431]
df_test = df[431:]


def next_stock_batch(batch_size, n_steps, df_base):
    t_min = 0
    t_max = df_base.shape[0]

    # The inputs will be formed by 8 sequences taken from
    # 7 time series [ISE.1,SP,DAX,FTSE,NIKKEI,BOVESPA,EU]
    x = np.zeros((batch_size, n_steps, 7))

    # We want to predict the returns of the Istambul stock
    # taken into consideration the previous n_steps days
    y = np.zeros((batch_size, n_steps, 1))

    starting_points = np.random.randint(0, t_max - n_steps - 1, size=batch_size)
    # print(starting_points)

    for k in range(batch_size):
        lmat = []
        for j in np.arange(n_steps + 1):
            lmat.append(df_base.iloc[starting_points[k] + j, 2:].values)
        lmat = np.array(lmat)
        x[k, :, :] = lmat[:n_steps, 1:]
        y[k, :, 0] = lmat[1 : n_steps + 1, 0]

    return x, y


# x, y = next_stock_batch(3, 10, df_train)
