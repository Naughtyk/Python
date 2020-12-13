#!/usr/bin/env python
# coding: utf-8

# In[71]:


# Импортируем библиотеку
import tkinter as tk 

# Задаём длину поля в ячейках
SIZE = 8
# и размер ячейки
CELL_SZ = 100

# Создаём объект класса Tk
root = tk.Tk()

# Создаём фон/поле/холст, на котором будут рисоваться объекты
canvas = tk.Canvas(root, width=CELL_SZ*SIZE, height=CELL_SZ*2)

flag = False # Флаг для отслеживания, была ли уже запущена анимация или нет
lantern = canvas.create_arc(100+(SIZE-2)*CELL_SZ, 100,
                            200+(SIZE-2)*CELL_SZ, 200,
                            start=45, extent=90, fill = 'red')
lantern2 = canvas.create_rectangle(150+(SIZE-2)*CELL_SZ, 50,
                                   150+(SIZE-2)*CELL_SZ, 100,
                                   fill = "black")
lantern3 = canvas.create_oval(130+(SIZE-2)*CELL_SZ, 30,
                              170+(SIZE-2)*CELL_SZ, 70,
                              fill = "black")
canvas.pack()

# Функция передвижения лампы по полю
def motion(i = 0):
    if flag == True:
        if canvas.coords(lantern)[2] > CELL_SZ:
            canvas.move(lantern, -1, 0)
            canvas.move(lantern2, -1, 0)
            canvas.move(lantern3, -1, 0)
            canvas.itemconfig(lantern3, fill = _from_rgb((i%255, i%255, i%255)))
            root.after(5, motion, i + 1)

# Функция, вызываемая в случае нажатия кнопки "Пуск"
def clicked():
    global flag # Чтобы при повторном нажатии уже ничего не происходило
    if flag == False:
        flag = True
        motion()
         
def stop(event):
    global flag
    if flag == True:
        flag = False
        
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb   
        
mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 
mainmenu.add_command(label = 'Пуск', command = clicked)

root.bind('<Double-Button-1>', stop)

root.mainloop()


# In[ ]:




