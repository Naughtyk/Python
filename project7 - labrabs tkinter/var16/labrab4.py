# Импортируем библиотеку
import tkinter as tk 
import calendar
days = []
year = 2020
month = 4
flag = False # Флаг для отслеживания, была ли запущена анимация

# Задаём размеры поля
BRD_ROWS = 5 # 5 строк - для дней недели + 1 строка для названий дней
BRD_COLS = 7 # 7 столбцов
# и размер ячейки
CELL_SZ = 100

# Создаём объект класса Tk
root = tk.Tk()

# Создаём фон/поле/холст, на котором будут рисоваться объекты
canvas = tk.Canvas(root, width = CELL_SZ*BRD_COLS, height = CELL_SZ*(BRD_ROWS + 1))

# Рисуем дни недели
for i in range(BRD_COLS):
    x1, y1 = i * CELL_SZ, 0 # Координаты верхнего левого угла квадрата
    x2, y2 = i * CELL_SZ + CELL_SZ, CELL_SZ # Координаты нижнего правого угла квадрата
    canvas.create_rectangle((x1, y1), (x2, y2), fill = 'lightgray') # Сам квадрат
    mylabel = canvas.create_text(((x2+x1)/2, (y2+y1)/2),
                                 text = calendar.day_abbr[i], font="Verdana 14")

# Цвета ячеек - белый и серый
cell_colors = ['white', 'grey']
ci = 0  # индекс цвета

month_days = calendar.monthrange(year, month)[1]
prew_month_days = calendar.monthrange(year, month - 1)[1]
week_day = calendar.monthrange(year, month)[0]

# Рисуем календарь
for row in range(BRD_ROWS):
    for col in range(BRD_COLS):
        # Меняем цвет и число в зависимости от апрельского или мартовского дня
        # Апрельские дни
        if (month_days + week_day > row * 7 + col >= week_day):
            text = str(row * 7 + col - week_day + 1)
            ci = 0
        # Мартовские дни
        else:
            text = str(prew_month_days + col - week_day + 1)
            ci = 1
        x1, y1 = col * CELL_SZ, (row+1) * CELL_SZ # Координаты верхнего левого угла квадрата
        x2, y2 = col * CELL_SZ + CELL_SZ, (row+1) * CELL_SZ + CELL_SZ # Координаты нижнего правого угла квадрата
        canvas.create_rectangle((x1, y1), (x2, y2), fill = cell_colors[ci]) # Сам квадрат
        # Помещаем число в центр ячейки
        mylabel = canvas.create_text(((x2+x1)/2, (y2+y1)/2), text = text,
                                     font="Verdana 14")

# i - Счётчик, указывающий на количество дней, прошедших с начала календаря
# (но не месяца)
def motion(i = week_day + 1):
    global ramka
    # Если была нажата кнопка пуск и не была нажата кнопка остановки
    if flag == True:
        # Если счётчик вышел за рамки календаря, то возвращаемся в начало месяца
        if i > month_days + week_day - 1:
            canvas.move(ramka, -2*CELL_SZ, -4*CELL_SZ)
            root.after(100, motion)
        # Если текущий день - воскресенье, то перейти на следующую строчку
        if i % 7 == 0:
            canvas.move(ramka, -CELL_SZ*6, CELL_SZ)
        # Иначе - двигаем рамку дальше
        else:
            canvas.move(ramka, CELL_SZ, 0)
        # Пока не пришли в последний день календаря - вызываем функцию рекурсивно
        if i < month_days + week_day - 1:
            root.after(100, motion, i + 1)
        # Если пришли в конец - снова вызываем, но с увеличенным счётчиком
        # Чтобы попасть в условие, при котором возвращаемся в начало месяца
        elif i == month_days + week_day - 1:
            root.after(100, motion, i + 2)

def stopmotion():
    global ramka, flag
    flag = False
    # Удаляем старую рамку
    canvas.delete(ramka)
    # Создаём новую в начале месяца
    ramka = canvas.create_polygon(points, outline = 'green', 
                                  fill = '', width = 3)

# Функция, вызываемая в случае нажатия кнопки "Запуск движения"
def clicked():
    global flag # Чтобы при повторном нажатии уже ничего не происходило
    if flag == False:
        flag = True
        motion()

canvas.pack() # Упаковка, чтобы всё было чётко и ровно
# Создаём рамку в первом числе мая
#ramka = canvas.create_rectangle(CELL_SZ*2, CELL_SZ*1, CELL_SZ*3, CELL_SZ*2,
                                #fill = '', outline = 'green', width = 3)


points = [(CELL_SZ*2.5, CELL_SZ*0.5), (CELL_SZ*3.25, CELL_SZ*1.25),
          (CELL_SZ*2.75, CELL_SZ*2.25), (CELL_SZ*2.25, CELL_SZ*2.25),
          (CELL_SZ*1.75, CELL_SZ*1.25)]
ramka = canvas.create_polygon(points, outline = 'green', 
    fill = '', width = 3)

# Создаём кнопку пуск
motion_button = tk.Button(root, text = 'Пуск', command = clicked,
                          font = "16", padx = "20", pady = "20")
# Упаковываем её под календарём 
motion_button.pack(side = 'left', padx = 10, pady = 10)

stop_button = tk.Button(root, text = 'Стоп', command = stopmotion,
                          font = "16", padx = "20", pady = "20")
stop_button.pack(side = 'right', padx = 10, pady = 10)

root.mainloop()