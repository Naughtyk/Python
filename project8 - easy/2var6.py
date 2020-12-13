Pi = 3.1415926535
while(1):
    w = float(input('w = '))
    h1 = float(input('h1 = '))
    r = float(input('r = '))
    h2 = float(input('h2 = '))
    if (w*w*h1 > Pi*r*r*h2):
        print("Коробка больше по объёму, чем ведро")
    elif (w*w*h1 == Pi*r*r*h2):
        print("Коробка и ведро одинаковы по объёму")
    else: 
        print("Коробка меньше по объёму, чем ведро")