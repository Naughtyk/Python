file = open('task3.txt')

P, N, k = file.readline().split(' ')
P = int(P)
N = int(N)
k = int(k)

univers = []

for i in range(P):
  command = file.readline()
  univers += [command[:-1]]

commands_number = file.readline().split(' ')

print(P, N, k)
print(univers)
print(commands_number)

dict = {}
for idx, item in enumerate(univers):
  if N == 0:
    break
  if item not in dict:
    dict[item] = 1
  else:
    dict[item] += 1
  if dict[item] > 2:
    continue
  else:
    print(item + ' #' + commands_number[idx])
    N -= 1