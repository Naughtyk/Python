"""
Программа, моделирующая последовательность
антагонистических игр с заданной матрицей платежей
и вычисляющая средний и суммарный выигрыш

Автор: Афанасьев И.Е.
Дата написания: 20.09.2020
"""

iterations = 565000 # Количество ходов
start_money = 1000 # Начальное количество денег у каждого игрока
matrix1 = [ [-2, 3], [3, -4] ] # Матрица платежей

# Инвертируем матрицу (Платежи для второго игрока)
q = len (matrix1)
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

# Вычисляем суммарный и средний выигрыш
sum_gain = 0
average_gain = []
x = [] # ось x

# Игра
for i in range(iterations):
    str1 = player1.math() # Вычисление текущего хода
    str2 = player2.math() # Вычисление текущего хода
    
    player1.strikeback(str2)
    player2.strikeback(str1)
    
    sum_gain += matrix1[str1][str2]
    average_gain += [sum_gain / (i + 1)]
    x += [i]

plt.plot(x[::100], average_gain[::100])
plt.show()