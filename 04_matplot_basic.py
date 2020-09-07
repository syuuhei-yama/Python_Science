import numpy as np
import matplotlib.pyplot as plt

#a = [1,2,3,4,5]
#b = [2,3,4,5,6]
#plt.plot(a, b,'o--')
#plt.show()
x = np.arange(10)

plt.plot(x, x**2, x, x**3, x, x**4)
#plt.plot(x, x**3)
plt.grid()
plt.title('折れ線のグラフ')
plt.xlabel('xのラベル')
plt.ylabel('yのラベル')
plt.legend(['x*2', 'x**3','X**4'], loc='upper center')
plt.xlim([2, 6])
plt.ylim([0, 1000])
#plt.show()
plt.savefig('test.png')