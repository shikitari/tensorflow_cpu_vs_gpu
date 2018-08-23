import numpy as np


x = np.linspace(0, 15, 15)
y = np.power(np.e, x)
y_int = y.astype('int32')

for i in y_int:
    print("{} ".format(i), end="")
