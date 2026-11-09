import numpy as np

data = np.array([
    [10, 20, 30, 40, 50],
    [40, 50, 60, 70, 80],
    [10, 20, 30, 40, 50],
])

print(data)
print(data.ndim)
print(data.shape)
print(data.size)
print(np.mean(data))
print(np.mean(data, axis=1))
print(np.mean(data, axis=0))
print(np.min(data))
print(np.max(data))
print(data[data >= 60])
print(data[data < np.mean(data)])
print(data[0])
print(data[:, -1])
print(data[1:3, 1:3])

data[1, 0] = 95
p = data + 5

print(p)
print(np.mean(p))
print(np.mean(p, axis=1))
print(np.max(np.mean(p, axis=1)))

numbers = np.arange(1, 17)

table = numbers.reshape(4, 4)
print(table[2:4, 2:4])
