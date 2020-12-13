from math import sin, exp, pi, tan, log

def f(x, y, c):
  a = c**5 + sin(y-c)**4
  b = sin(x + y)**3 + abs(x - y)
  if b == 0 or a / b > 1000000:
    return '∞'
  return a / b
  
x1 = exp(2)
y1 = 5.01
c1 = 1.6

print('1: f =', f(x1, y1, c1))

x2 = 0
y2 = 0
c2 = pi / 2

print('2: f =', f(x2, y2, c2))

x = []
y = []
c = []

print('i     x      y        c      f(x, y, c)')

for i in range(1, 28):
  x = 1 - (i**2) / (i**0.5)
  y = tan(pi/6 * (i - 1) / (i + 1))
  if i == 1:
    c = 2*log(2)/log(5)
  else:
    c = log(i**2, 5)/log(i, 2)
  f1 = f(x, y, c)
  if f1 == '∞':
    print(i, '{0:.5f}'.format(x), '{0:.5f}'.format(y), '{0:.5f}'.format(c), '    '+f1, '\n')
  else:
    print(i, '{0:.5f}'.format(x), '{0:.5f}'.format(y),'{0:.5f}'.format(c), '{0:.5f}'.format(f1), '\n')