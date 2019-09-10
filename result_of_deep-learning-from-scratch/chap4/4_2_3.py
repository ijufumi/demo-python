# 注意：動かない

import sys, os

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    if t.size == y.size:
        t = t.argmax(axis=1)

    print(t)
    # print(np.arange(batch_size))
    # print(y[np.arange(batch_size), t])

    return y
    # return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
    #return -np.sum(t * np.log(y + 1e-7)) / batch_size


sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

#print(x_train.shape)
#print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

# print(batch_mask)
cross_entropy_error(x_batch, t_batch)
#print(cross_entropy_error(x_batch, t_batch))
