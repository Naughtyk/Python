a = float(input('a = '))
b = float(input('b = '))
h = float(input('h = '))

if(a < b):
  a, b = b, a

bokovaya = (((b - a) / 2)**2 + h**2)**0.5
S = (a + b)*h/2
P = a + b + 2*bokovaya
diag = (bokovaya**2 + a*b)**0.5

p = (a + diag + bokovaya) / 2

r = p/(2*(p*(p-a)*(p-diag)*(p-bokovaya))**0.5)

print('bokovaya: ', bokovaya)
print('S: ', S)
print('P: ', P)
print('diagonal: ', diag)
print('radius: ', r)