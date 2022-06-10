import numpy as np


def f(x):
    return (np.exp(x) - 4 / (np.exp(2 * x))) ** 2


def df(x):
    return (2 * np.exp(2 * x) + 8 * np.exp(-x) - 64 * np.exp(-4 * x))


def GradientDescent(eta, x0):
    x = [x0]
    for it in range(1000):
        x_new = x[-1] - eta*df(x[-1])
        if abs(df(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, it)


if __name__ == "__main__":
    (x, it) = GradientDescent(.01, .5)
    print(
        f'Solution x = {x[-1]}, cost = {f(x[-1])}, obtained after {it} iterations')
