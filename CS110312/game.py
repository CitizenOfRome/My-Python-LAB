T = int(raw_input())
def play(n):
    a = int(n/2)
    b = n-a
    if a%2==0:
        a -= 1
        b += 1
    return [a,b]
for t in xrange(T):
    [n1,n2] = [int(x) for x in raw_input().split()]
    odd = True
    ret = "Alice"
    #print n1, n2
    while True:
        if odd: ret = "Alice"
        else: ret = "Bob"
        if n1==1:   n = n2
        elif n2==1: n = n1
        elif n1%2==0:   n = n1
        elif n2%2==0:   n = n2
        else:   n = min(n1,n2)
        [n1, n2] = play(n)
        #print n1, n2
        if n1<=1 and n2<=1: break
        odd = not odd
    print ret