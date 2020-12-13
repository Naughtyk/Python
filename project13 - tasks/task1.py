
f = open('task1_1.txt', 'r')

N = int(f.readline())

dict1 = {} # сотрудник - расстояние
dict2 = {} # такси - тариф

for i in range(N):
    dict1[i] =  int(f.readline())
for i in range(N):
    dict2[i] =  int(f.readline())
f.close()
list_dict1 = list(dict1.items())
list_dict1.sort(key = lambda i: i[1], reverse = True)

list_dict2 = list(dict2.items())
list_dict2.sort(key = lambda i: i[1])

print(list_dict1)
print(list_dict2)

dict3 = {} # сотрудник - такси
for i in range(N):
    dict3[list_dict1[i][0]] = list_dict2[i][0]
    
list_dict3 = list(dict3.items())
list_dict3.sort(key = lambda i: i[0])
    
print(list_dict3)

f = open('task1_2.txt', 'w')
for i in list_dict3:
    f.write(str(i[1]) + '\n')
f.close()
    
    
    
    
    
    