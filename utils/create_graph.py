import numpy as np
import matplotlib.pyplot as plt


data1 = np.loadtxt("../report_cpu.txt",delimiter=",", skiprows=1)
x1 = data1[:,0]
y1 = data1[:,1]
p1 = plt.plot(x1, y1, marker='o')

data2 = np.loadtxt("../report_gpu.txt",delimiter=",", skiprows=1)
x2 = data2[:,0]
y2 = data2[:,1]
p2 = plt.plot(x2, y2, marker='o')

plt.title("CPU i7 3.5 GHz VS GTX 775M")
plt.xlabel("num of operations")
plt.ylabel("sec")
plt.legend((p1[0], p2[0]), ("CPU", "GPU"), loc=2)
plt.show()
