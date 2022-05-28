import numpy as np


def pressure(temperature):
    f = np.divide(2116, 144)
    t = temperature + 459.70
    p = np.divide(t, 518.60)
    p0 = np.power(p, 5.256)
    pres = np.multiply(f, p0)
    return pres
