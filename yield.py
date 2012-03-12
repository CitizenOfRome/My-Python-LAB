def get_primes_till(max):
    '''Yeilds primes'''
    i = 2
    while i<=max:
        for j in xrange(2,i):
            if i%j==0:  break
        else:   yield i
        i = i+1
        
for i in get_primes_till(999):
    print i,