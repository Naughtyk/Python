from math import atan

x = [-1.4, 0.8, 2.4, 4.9, 7.3, -4.1, 9.0, 6.3]
y = [-4.3, 3.0, -6.4, -0.9, -5.4, 4.1, 8.7, 2.8]
r = []
alphas = []
for i in range(len(x)):
  r += [(x[i]**2 + y[i]**2)**0.5]
  alphas += [atan(y[i]/x[i])]
  print('r[i]: ', r[i])
  print('alpha[i]: ', alphas[i])

maximum = max(r)
counts = r.count(maximum)
index = -1
for i in range(counts):
  index = r.index(maximum, index + 1)
  print('max vector: ', x[index], y[index])

minalpha = alphas.index(min(alphas))
print('min ugol: ', x[minalpha], y[minalpha])