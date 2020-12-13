# 1 task
print("1 task:")

# Объявляем функцию, проверяющую подаваемое ей на вход число
def filter_num(in_num):
    # Если число чётное - возвращает True, иначе - False
    if(in_num % 2) == 0:
        return True
    else:
        return False
    
# Создаём список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# filter - стандартная функция Python, принимаем в качестве аргументов
# функцию, по принципу которой происходит фильтрация
# и список, который необходимо фильтровать
out_filter = filter(filter_num, numbers)

# Выводим результат работы фильтра
print("список: ", numbers)
print("Отфильтрованный список: ", list(out_filter))


# 2 task
print("2 task:")

# Объявляем генератор, аргументы - 2 списка
def generator(l1, l2):
    # Вычисляем, длина какого списка больше
    maxlen = max(len(l1), len(l2))
    # Пробегаемся по всем элементам обоих списков
    for i in range(maxlen):
        # Пытаемся вернуть ответ, если не получается - просто пропускаем итерацию
        try:
            yield (l1[i], l2[i])
        except IndexError:
            pass
        
# Создаём два списка разной длины
list1 = [1, 2, 3, 4]
list2 = [3, 2, 1]

# Создаём генератор, подаём ему наши списки
gen = generator(list1, list2)

# Выводим все пары чисел двух списков
for i in gen:
    print(i)
    
# 3 task
print("3 task:")
    
# Объявляем генератор, аргументы - список lst и два шага step1 и step2
def generator2(lst, step1, step2):
    # Флаг, который отвечает за смену шага по очереди, сначала step1, потом step2
    # на каждой итерации
    flag = True
    
    # Индекс элементов списка
    i = 0
    
    # До тех пор, пока индекс не вышел за пределы списка
    while i < len(lst):
        # Возвращаем элемент
        yield lst[i]

        # Если flag == True, то увеличиваем индекс на step1 и меняем flag 
        if flag:
            i += step1
            flag = False
        else:
            i += step2
            flag = True
          
# проверяем, как работает
numbers2 = [1, 2, 4, 5, 7, 8, 10, 11]      
gen2 = generator2(numbers2, 1, 2)
    
for i in gen2:
    print(i)
    
# 4 task
print("4 task:")    

# Объявляем генератор. На входе - список lst и диапозон скользящего среднего
def generator3(lst, diap):        
    # Пробегаемся по всем элементам списка
    for i in range(len(lst)):
        sum = 0
        # Если индекс меньше диапозона - пока пропускаем
        if i < diap:
            pass
        # Иначе - считаем сумму последних "diap" элементов, и выводим их среднее
        else:
            for j in range(i):
                sum += lst[i - j]
            yield sum / diap
            
# Проверяем
numbers3 = [1, 2, 4, 5, 7, 8, 10, 11]
gen3 = generator3(numbers3, 2)

for i in gen3:
    print(i)
    

# 5 task
print("5 task:")

numbers4 = [-5, -4, -2, 0, 1, 3, 5, 10]

# подаём в фильтр сразу Лямбда-функцию и список чисел
out_filter2 = filter(lambda x: x > 0, numbers4)

# Выводим результат работы фильтра
print("список: ", numbers4)
print("Отфильтрованный список: ", list(out_filter2))









    
    