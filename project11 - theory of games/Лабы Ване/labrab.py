"""
Программа, моделирующая последовательность
антагонистических игр с заданной матрицей платежей

Автор: Афанасьев И.Е.
Дата написания: 20.09.2020
"""

iterations = 10000 # Количество ходов
start_money = 10000 # Начальное количество денег у каждого игрока
matrix1 = [ [-4, 5], [8, -7] ] # Матрица платежей

# Инвертируем матрицу (Платежи для второго игрока)
q = len(matrix1)
matrix2 = []
for i in range(q):
    matrix2.append([])
for i in matrix1:
    for pos, j in enumerate(i):
        matrix2[pos % q].append(- j)

# Класс игрок с матрицей платежей, текущим количеством
# денег, коэффициентами для принятия решения на основе
# стратегии противника и последним ходом
class gamer:
    def __init__(self, matrice, money):
        self.m = matrice
        self.money = money
        self.koef = [0] * len(matrice[0])
        self.last = 0
    def strikeback(self, enemy_strat):
        self.koef[enemy_strat] += 1
        self.money += self.m[self.last][enemy_strat]
        return self.money
    # Вычисление оптимального хода на основе
    # предыдущих ходов противника
    def math(self):
        M = []
        for i in self.m:
            process = 0
            for j in range(len(self.koef)):
                process += self.koef[j] * i[j]
            M.append(process)
        self.last = M.index(max(M))
        return self.last

# Импортируем графическую библиотеку
import matplotlib.pyplot as plt
# Создаём два объекта класса "игрок"
player1 = gamer(matrix1, start_money)
player2 = gamer(matrix2, start_money)

# Инициализируем фигуру, на которой будем рисовать
fig = plt.figure()
plt.ion()
color = ['red', 'green', 'blue', 'brown']
y = [] # Ось y
x = [] # Ось x
for i in range(len(color)):
    y.append([])
    x.append([])

# Собственно, игра
for i in range(iterations):
    str1 = player1.math()
    str2 = player2.math()
    
    y[str1].append(player1.strikeback(str2))
    x[str1].append(i)
    
    y[str2 + 2].append(player2.strikeback(str1))
    x[str2 + 2].append(i)

for i in range(len(x)):
    plt.plot(x[i], y[i], c = color[i])
plt.show() # Отображение графика
print('Длительность тестовой серии игры: ', iterations)
print(
          'Стратегии первого игрока: %s\nДеньги первого игрока: %d\n' % 
          (player2.koef, player1.money)
          )
print(
          'Стратегии второго игрока: %s\nДеньги второго игрока: %d' % 
          (player1.koef, player2.money)
          )