import numpy as np

class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

relu = Relu()
value = np.array([[1.0, 0.5], [-2.0, 3.0]])

v1 = relu.forward(value)
print(v1)
v2 = relu.backward(value)
print(v2)