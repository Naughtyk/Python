while(1):
    x1 = float(input('x1 = '))
    y1 = float(input('y1 = '))
    r1 = float(input('r1 = '))
    x2 = float(input('x2 = '))
    y2 = float(input('y2 = '))
    r2 = float(input('r2 = '))
    if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 > r1 + r2:
        print("Окружности не пересекаются")
    elif ((x1 - x2)**2 + (y1 - y2)**2)**0.5 == r1 + r2: 
        print("Окружности касаются")
    else:
        print("Окружности пересекаются")