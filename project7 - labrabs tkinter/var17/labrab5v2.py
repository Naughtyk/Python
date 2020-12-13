import tkinter as tk

BRD_ROWS = BRD_COLS = 8
CELL_SZ = 50
 
root = tk.Tk()
 
canvas = tk.Canvas(root, width=CELL_SZ*BRD_ROWS + 150, height=CELL_SZ*BRD_COLS)

cell_colors = ['white', 'black']
ci = 0  # color index
 
for row in range(BRD_ROWS):
    for col in range(BRD_COLS):
        x1, y1 = col * CELL_SZ, row * CELL_SZ
        x2, y2 = col * CELL_SZ + CELL_SZ, row * CELL_SZ + CELL_SZ
        canvas.create_rectangle((x1, y1), (x2, y2), fill = cell_colors[ci])
 
        ci = not ci

    ci = not ci

canvas.pack()
canvas.focus_set()
shashka = canvas.create_oval(10, 10, 40, 40, outline="gray", fill="brown", width=2)

def motion():
    canvas.move(shashka, 50, 50)
    if canvas.coords(shashka)[2] < 350:
        root.after(700, motion)
    else:
        root.after(700, backmotion)
        
def backmotion():
    canvas.move(shashka, -50, -50)
    if canvas.coords(shashka)[2] > 50:
        root.after(700, backmotion)
    else:
        root.after(700, motion)

def clicked():  
    #button.configure(state = 'disabled')
    motion()

#button = tk.Button(root, text = "Запуск движения", width = 20, height = 5, command = clicked)
#button.place_configure(x = 400, y = 150)

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("context")
        self.menu = tk.Menu(self.parent, tearoff = 0)
        self.menu.add_command(label = "Запуск движения", command = clicked)
        self.parent.bind("<Button-3>", lambda event: self.menu.post(event.x_root, event.y_root))
        self.pack()

app = Main(root)
root.mainloop()