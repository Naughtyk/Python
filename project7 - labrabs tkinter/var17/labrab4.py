from tkinter import *
import calendar
import datetime
import time
root = Tk()
root.title('Calendar')
days = []
now = datetime.datetime.now()
year = now.year
month = now.month

# Заполнение календаря
def fill():
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    prew_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    # Рисуем текущий месяц
    for n in range(month_days):
        days[n + week_day]['text'] = n + 1
        days[n + week_day]['fg'] = 'black'
        days[n + week_day]['background'] = 'lightgray'
    # Рисуем дни предыдущего месяца
    for n in range(week_day):
        days[week_day - n - 1]['text'] = prew_month_days - n
        days[week_day - n - 1]['fg'] = 'gray'
        days[week_day - n - 1]['background'] = '#f3f3f3'
    # Рисуем дни следующего месяца
    for n in range(6*7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n+1
        days[week_day + month_days + n]['fg'] = 'gray'
        days[week_day + month_days + n]['background'] = '#f3f3f3'

# Месяц, год
info_label = Label(root, text='0', width=1, height=1, 
            font=('Verdana', 16, 'bold'), fg='blue')
info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

canvas = Canvas(root, width=60, height=60, bg='white')

# Названия sun mon tue...
for n in range(7):
    lbl = Label(root, text = calendar.day_abbr[n], width=1, height=1, 
                font=('Verdana', 10, 'normal'), fg='darkblue')
    lbl.grid(row = 1, column = n, sticky='nsew')

# Сами числа 1,2,3...
for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2, 
                    font=('Verdana', 16, 'bold'))
        lbl.grid(row = row + 2, column = col, sticky='nsew')
        days.append(lbl)

def motion(i = 0, background = None, bd = 0):
    if i > 0:
        days[i - 1]['background'] = background
    if i < len(days):
        background = days[i]['background']
        days[i]['background'] = 'green'
        root.after(1000, motion, i + 1, background, bd)
    else:
        return

canvas.create_rectangle(0, 0, 60, 60, 
            outline="blue", fill="gray", width=3)
canvas.grid(row = 2, column = 2)

motion_button = Button(root, text = 'motion', command = motion)
motion_button.grid(row = 0, column = 0, sticky = 'nsew')

fill()

root.mainloop()

