
file = open('task4.txt')

n, m, k = file.readline().split(' ')
n = int(n)
m = int(m)
k = int(k)

countries = file.readline()[:-1]
countries = list(countries)

matrix = [[0 if i == j else 1000 for i in range(n)] for j in range(n)]

for i in range(m):
    road = file.readline()[:-1].split(' ')
    matrix[int(road[0]) - 1][int(road[1]) - 1] = int(road[2])
    matrix[int(road[1]) - 1][int(road[0]) - 1] = int(road[2])
    
riots = file.readline()[:-1].split(' ')
    
# Алгоритм Флойда-Уоршелла
# d - матрица кратчайших путей
d = matrix
for i in range(1, n + 1):
    for j in range(n):
        for k in range(n):
              if d[j][k] > d[j][i - 1] + d[i - 1][k]:
                  d[j][k] = d[j][i - 1] + d[i - 1][k]

mass = []
for i in range(n):
    for j in range(i):
        mass += [[j, i, d[j][i]]]
mass.sort(key = lambda i: i[2])

for j in mass:
    if countries[j[0]] == countries[j[1]]:
        print(j[2], j[0] + 1, j[1] + 1)
        break

for riot in riots:
    if countries[int(riot) - 1] == 'L':
        countries[int(riot) - 1] = 'R'
    else:
        countries[int(riot) - 1] = 'L'
    for j in mass:
        if countries[j[0]] == countries[j[1]]:
            print(j[2], j[0] + 1, j[1] + 1)
            break

    
    
    

