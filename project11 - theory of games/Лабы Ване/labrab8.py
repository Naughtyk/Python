"""
Программа, вычисляющая вектор Шепли

Автор: Афанасьев И.Е.
Дата написания: 20.09.2020
"""

# импортируем перестановки
from itertools import permutations

# функция, вычисляющая факториал числа
def fact(i):
  if i <= 1:
    return 1
  return i * fact(i - 1)

# Задаём расстояния до домов ("Малое Гадюкино")
X = [40, 90, 150, 240, 300, 500]
# Порядковые номера домов
X_i = [i for i in range(len(X))]

# Факториал от числа домов
factX = fact(len(X))

# Перестановки всех домов (И дублирование для номеров домов)
perm = permutations(X)
perm_i = list(permutations(X_i))

# Характеристическая функция
hf = []
for i in perm:
  hf1 = []
  for j in range(len(i)):
    if j == 0:
      hf1 += [i[j]]
    else:
    # Отражает вклад каждого жителя в постройку дороги
      hf1 += [i[j] - max(i[:j]) if i[j] - max(i[:j]) > 0 else 0]
  hf += [hf1]

# Инициализируем вектор Шепли
shapley = [0]*len(X)

# Пробегаемся по всем перестановкам
for i in range(factX):
  for j in range(len(X)):
    for k in range(len(shapley)):
      if perm_i[i][j] == k:
        shapley[k] += hf[i][j]

# Усредняем
for i in range(len(shapley)):
  shapley[i] /= factX

print(shapley)
