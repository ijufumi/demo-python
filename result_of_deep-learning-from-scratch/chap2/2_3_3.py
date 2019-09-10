import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def calc(x1, x2):
    print("{} AND {} = {}".format(x1, x2, AND(x1, x2)))
    print("{} NAND {} = {}".format(x1, x2, NAND(x1, x2)))
    print("{} OR {} = {}".format(x1, x2, OR(x1, x2)))


calc(0, 0)
calc(1, 0)
calc(0, 1)
calc(1, 1)

