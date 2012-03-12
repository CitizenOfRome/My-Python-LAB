def ones(num):
    '''Returns the number of ones in the binary(twos complement) of a number'''
    res = ""
    nve=False
    if num<0:
        nve=True
        num = -num-1
    uno = 0
    cnt = 0
    # while num!=0:
        # if (num%2==0)==nve:    uno+=1
        # num = int(num*0.5)
        # cnt += 1
    res = bin(num)[2:]
    #res = '{0:b}'.format(num)
    uno = res.count("1")
    cnt = len(res)
    if nve: uno+=32-cnt
    return uno
no = int(raw_input())

for i in xrange(no):
    [j,k] = map(int, raw_input().split(" "))
    ret = 0
    while j<=k:
        ret += ones(j)
        j+=1
    print(ret)
    
# 1
# -2147483648 2147483647
