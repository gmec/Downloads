from math import sqrt

print('This software solves 2nd degree equations like ax^2 + bx + c = 0\n')
a = float(input('Type the value of a: '))
b = float(input('Type the value of b: '))
c = float(input('Type the value of c: '))

delta = b*b - 4*a*c

try:
    sdelta = sqrt(delta)
    r1 = (-b + sdelta)/(2*a)
    r2 = (-b - sdelta)/(2*a)
    print('Your equation: %fx^2 + %fx + %f = 0\n' % (a, b, c))
    print('Solution: \nr1 = %f\nr2 = %f' % (r1, r2))
    input('Press <Return> to exit...')
except ValueError:
    print('\nDelta is negative. Result is complex.')
    input('Press <Return> to exit...')


