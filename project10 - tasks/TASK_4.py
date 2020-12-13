from numpy import tan, sin, pi
import numpy as np

def f_b(i):
    return sin(((3 ** (1/3)) * i * pi / 2) + 1)
  
def f_a(i, j):
    return tan((i + 1) / (j + 2))
  
n = int(input('N = '))

a = np.fromfunction(f_a, (n, n))
b = np.fromfunction(f_b, (n,))

print(a)
print(b)

x = np.dot(np.linalg.matrix_power(a, 3), b)
y = np.linalg.det(a) * np.dot(np.linalg.matrix_power(np.linalg.inv(a), 2), b)
answer1 = x + y
print('1:', answer1)

x = a[0] * a[:, 1]
y = sum(b)
print('2.1:', x)
print('2.2:', y)
c = b + a.max() - np.mean(a)
print('3:', c)
print('4:', b + c)
maximum = b.max()
counts = list(b).count(maximum)
print('5:', counts)