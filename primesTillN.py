def primesTillN(n):
    '''Returns all the primes upto n'''
    result = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                #print i, ' aint a prime with ', j
                break
        else:#works on successful completion of loop
            result.append(i)
    return result
print primesTillN(500)