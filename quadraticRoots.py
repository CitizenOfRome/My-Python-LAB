import math
def quadraticRoots(a, b, c):
    '''Returns the complex quadratic roots of ax2+bx+c'''
    #x = (-b+/-root(b2-4ac))/2a
    d = math.pow(b, 2) - 4 * a * c
    if d < 0:
        j = 1
    else:
        j = 0
    d2 = math.sqrt(math.fabs(d))
    real = -b/(2*a)
    imag = d2/(2*a)
    if j:
        return [complex(real, imag), complex(real, -imag)]
    else:
        return [real + imag, real - imag]
print quadraticRoots(1, 2, 3)