"""
Программа, производящая вычисление по формуле
вероятности общей победы и строящая графики зависимости
в задаче о разорении игрока

Автор: Афанасьев И.Е.
Дата написания: 20.09.2020
"""

# Функция расчёта вероятности общей победы
def fun(p, k, N):
  q = 1 - p
  return ((q/p)**k - 1) / ((q/p)**N - 1)

# импорт графической библиотеки
import matplotlib.pyplot as plt

# Задаём пул различных параметров задачи
# P - массив вероятность выигрыша первого игрока
# K - массив количества денег первого игрока (n - k - деньги второго игрока)
# N - массив общего количества денег игроков
P = [i/100 for i in range(55, 100, 5)]
K = [i for i in range(1, 10, 1)]
N = [i for i in range(5, 15, 1)]

# для первого задания

# Фиксируем n и k, p - меняем
funcP = []
for p in P:
  funcP += [fun(p, K[len(K) // 2], N[len(N) // 2])]
  
# Фиксируем p и n, k - меняем
funcK = []
for k in K:
  funcK += [fun(P[len(P) // 2], k, N[len(N) // 2])]
  
  # Фиксируем p и k, n - меняем
funcN = []
for n in N:
  funcN += [fun(P[len(P) // 2], K[len(K) // 2], n)]

# Строим графики
fig = plt.figure()
plt.subplot(4, 1, 1)
plt.plot(P, funcP)
plt.subplot(4, 1, 2)
plt.plot(K, funcK)
plt.subplot(4, 1, 3)
plt.plot(N, funcN)
  
# для второго задания

# k и n меняются в соотношении 1 к 10
K = [i for i in range(1,10,1)]
N = [i for i in range(10,100,10)]
p = 0.55

# Вычисляем по формуле
funcNK10 = []
for i in range(len(K)):
  funcNK10 += [fun(p, K[i], N[i])]

# Строим графики
plt.subplot(4, 1, 4)
plt.plot(K, funcNK10)

# Выводим на экран
plt.show()

# 3 задание - при p -> 1