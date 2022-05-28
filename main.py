import numpy as np
import matplotlib.pyplot as py
from Aspectratio import func_ar
root = float(input("Enter the root chord length (in inches): "))
tip = float(input("Enter the tip chord length (in inches): "))
height = float(input("Enter the height (in inches): "))
AR = func_ar(root, tip, height)
thicc = float(input("Enter thickness of non-tapered fins(in inches): "))
G = float(input("Enter Shear Modulus(in psi): "))
lam = np.divide(tip, root)
alt = float(input("Enter Altitude: "))
temp = 59.0 - np.multiply(0.00356, alt)
T = temp + 460
print(temp)
from Pressure import pressure
P = abs(pressure(temp))
print(P)
GRT = T*1.40*1716.59
a = np.sqrt(GRT)
print(a)
tr = np.divide(thicc, root)
tc = np.power(tr, 3)
AR1 = AR + 2.000
den_den = 2.000*AR1*tc
lamb = lam + 1.000
den_num = 1.337*AR*AR*AR*P*lamb
den = np.divide(den_num,den_den)
num = G
frac = np.divide(num,den)
fraction = np.sqrt(frac)
v = np.multiply(a, fraction)
print(v)
