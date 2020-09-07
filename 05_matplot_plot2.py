import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x

plt.subplot(2,1,1)
plt.plot(x, y,color=(255/255,127/255,80/255,0.3),linestyle='--')
plt.plot(x, y+1, 'ko:')
plt.plot(x, y-1, 'c<-')
plt.plot(x, y-2, 'y>-')

ax = plt.subplot(2,1,2)
x = np.arange(100)
y = np.random.randint(0,10,100)
plt.plot(x,y)
ax.grid()
ax.set_ylabel('2つめのグラフのy')
ax.set_xlabel('2つめのグラフのx')
ax.set_title('2つめのグラフtitle')
ax.legend(['y'],loc='best')

x = np.arange(100)
y = x ** 2

ax = plt.subplot(2,2,3)
ax.set_yscale('log')
plt.plot(x,y)

x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

ax = plt.subplot(2,2,4)
ax.set_title('sin')
plt.plot(x,y)

plt.savefig('test.jpg')



plt.show()