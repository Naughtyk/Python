# Открываем файл
f = open('task2.txt', 'r')

# Считываем построчно 
first_str = f.readline()
left_formula = first_str

# Удаляем ненужные символы
left_formula = left_formula.replace('(', "")
left_formula = left_formula.replace(')', "")
left_formula = left_formula.replace('\n', "")

left_dict = {}

# Делим строку по на отдельные члены
left_formula = left_formula.split("+")

# Пробегаем по всем членам левой части уравнения
for item in left_formula:
    multiplier = 1 # множитель перед членом
    # Пробегаем по всем символам
    for idx in range(len(item)):
        long_elem = ''  # Это если элемент состоит из более чем 1 символа (напр. Si)
        # Если это число
        if item[idx].isdigit():
            # Если предыдущий символ - цифра, то пропускаем
            if idx != 0 and item[idx - 1].isdigit():
                continue
            # Если число - длинное (более 1 цифры)
            if idx != len(item) - 1:
                i = idx
                while item[i].isdigit():
                    long_elem += item[i]
                    i += 1
            else:
                long_elem += item[idx]
            # Если оно в начале - тогда это множитель
            if idx == 0:
                multiplier = int(long_elem)
            else:
                left_dict[item[idx - 1]] += (int(item[idx]) - 1) * multiplier
        else:
            # Если это нижний регистр - то это часть уже существующего элемента
            if item[idx].islower():
                continue
            # Если это не конец и следующий символ - в нижнем регистре
            if idx != len(item) - 1 and item[idx + 1].islower():
                # Тогда этот элемент - длинный
                long_elem = item[idx] + item[idx + 1]
                # Если его ещё нет в словаре, то добавляем
                if long_elem not in left_dict:
                    left_dict[long_elem] = 1 * multiplier
                else:
                    left_dict[long_elem] += 1 * multiplier
            else:
                if item[idx] not in left_dict:
                    left_dict[item[idx]] = 1 * multiplier
                else:
                    left_dict[item[idx]] += 1 * multiplier

N = int(f.readline())

right_formulas = []
right_strings = []
for i in range(N):
    right_formulas += [f.readline()]

dict_answers = {}

# Пробегаем по всем правым формулам
for index, right_formula in enumerate(right_formulas):
    right_strings += [right_formula]
    right_dict = {}
    right_formula = right_formula.replace('(', "")
    right_formula = right_formula.replace(')', "")
    right_formula = right_formula.replace('\n', "")

    right_formula = right_formula.split("+")
    # Пробегаем по всем членам правой части уравнения
    for item in right_formula:
        multiplier = 1 # множитель перед членом
        # Пробегаем по всем символам
        for idx in range(len(item)):
            long_elem = ''  # Это если элемент состоит из более чем 1 символа (напр. Si)
            # Если это число
            if item[idx].isdigit():
                # Если предыдущий символ - цифра, то пропускаем
                if idx != 0 and item[idx - 1].isdigit():
                    continue
                # Если число - длинное (более 1 цифры)
                if idx != len(item) - 1:
                    i = idx
                    while item[i].isdigit():
                        long_elem += item[i]
                        i += 1
                else:
                    long_elem += item[idx]
                # Если оно в начале - тогда это множитель
                if idx == 0:
                    multiplier = int(long_elem)
                else:
                    right_dict[item[idx - 1]] += (int(long_elem) - 1) * multiplier
            else:
                # Если это нижний регистр - то это часть уже существующего элемента
                if item[idx].islower():
                    continue
                # Если это не конец и следующий символ - в нижнем регистре
                if idx != len(item) - 1 and item[idx + 1].islower():
                    # Тогда этот элемент - длинный
                    long_elem = item[idx] + item[idx + 1]
                    # Если его ещё нет в словаре, то добавляем
                    if long_elem not in right_dict:
                        right_dict[long_elem] = 1 * multiplier
                    else:
                        right_dict[long_elem] += 1 * multiplier
                else:
                    if item[idx] not in right_dict:
                        right_dict[item[idx]] = 1 * multiplier
                    else:
                        right_dict[item[idx]] += 1 * multiplier
    if right_dict == left_dict:
        dict_answers[index] = '=='
    else:
        dict_answers[index] = '!='
    

for i in range(N):
    print (first_str[:-1] + dict_answers[i] + right_strings[i][:-1])
    
    
  