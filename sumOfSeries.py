import math
def factorial(x):
	'''Returns the factorial of the given number, recursively'''
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)
def sumOfSeries(x, n):
    '''Returns the sum of the 1st n terms of the series 1-x2/2!+x4/4!-x6/6!+x8/8!-x10/10!'''
    #ith term is given by: pow(-1, i-1)*pow(x, i*2)/(i*2)!
    result = 1
    for i in range(2, n+1):
        result += math.pow(-1, i-1) * math.pow(x, i*2) / factorial(i*2)
    return result
print sumOfSeries(2, 3)