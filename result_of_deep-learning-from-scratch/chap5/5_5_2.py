import numpy as np

class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx

sigmoid = Sigmoid()
v1 = sigmoid.forward(100)
print(v1)
v2 = sigmoid.backward(v1)
print(v2)