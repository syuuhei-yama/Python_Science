import numpy as np

x = np.array([0,1,0,1])
y = np.array([0,0,1,1])

print(np.bitwise_and(x, y))
print(np.bitwise_or(x, y))
print(np.bitwise_xor(x, y))
print(np.bitwise_not(x))

print(x & y)
print(x | y)
print(x ^ y)
print(~ x)