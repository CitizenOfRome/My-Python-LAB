def fibonacci(n):
    '''Returns the fibonacci series of n terms'''
    result = []
    if n > 0:
        result.append(0)
    if n > 1:
        result.append(1)
    if n > 2:
        for i in range(2, n):
            result.append(result[i-1] + result[i-2])
    return result
print fibonacci(5)