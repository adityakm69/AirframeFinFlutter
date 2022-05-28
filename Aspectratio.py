import numpy as np


def func_ar(root, tip, height):
    """
    :param root: root chord length
    :param tip: tip chord length
    :param height: semi span
    :return: aspect ratio
    """
    num = np.multiply(root + tip, height)
    S = num/2
    AR = np.divide(height*height, S)
    return AR