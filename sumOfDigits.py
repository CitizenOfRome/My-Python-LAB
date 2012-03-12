import math
def sumOfDigits(num):
    '''Returns the sum of the digits of an integer'''
    num = math.floor(num)
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result
print sumOfDigits(123)
#print "Hello world"