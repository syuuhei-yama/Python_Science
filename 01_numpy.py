import numpy as np

my_list = [1,2,3]
arr = np.array(my_list)
print(arr)
print(type(arr))

arr = np.arange(0,10)
print(arr)

print(arr.shape)
print(arr.ndim)
print(arr.dtype)
print(arr.size)
print(arr.nbytes)

print(np.arange(0, 10, 2))

print(np.linspace(0, 11, 10))

print(np.random.randint(0, 3, (5, 5, 5)))

print(np.random.rand()) #0~1のランダム値
print(np.random.randn())# 正規分布

np.random.seed(101)
arr = np.random.randint(0, 100, 10)
print(arr)

np.random.randint(0, 100,10)

print(arr)
print(arr.max())#最大値
print(arr.min())#最小値
print(arr.mean())#平均
print(arr.argmax())#最大値の場所
print(arr.argmin())#最小値のインデックス

print(arr.reshape(2,5)) # 2行5列

mat = arr.reshape(2,5)
print(mat[0][2])# 0行目２つめ
print(mat[1,2])
print(mat[1,:])
print(mat[:,3])
print(mat[0,2:4])

filter = mat > 50
print(mat[mat < 10])