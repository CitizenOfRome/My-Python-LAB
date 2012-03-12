import itertools
C = int(raw_input())
for c in xrange(C):
    N = int(raw_input())
    cities = [int(x) for x in raw_input().split()]
    cables = [int(x) for x in raw_input().split()]
    # dist = sum([sum([(cables[i]-cables[j])*(cities[i]-cities[j]) if cables[i]>cables[j] else (cables[j]-cables[i])*(cities[i]-cities[j])  for i in xrange(j,N)]) for j in xrange(N)])
    # pairs = []
    # sums = 0
    # for i in xrange(N-1):
        # j=i+1
        # if cables[i]>cables[j]:m=cables[i]
        # else:m=cables[j]
        # res=(m*(cities[i]-cities[j]))
        # if res<0:res=-res
        # pairs+=[res]
        # sums += sum([sum(pairs[k:i+1]) for k in xrange(i+1)])
    # dist = (sum(pairs)+sums)
    dist = 0
    for itr in itertools.combinations(xrange(N), 2):
        [i,j] = itr
        if cables[i]>cables[j]:m=cables[i]
        else:m=cables[j]
        res=(m*(cities[i]-cities[j]))
        if res<0:res=-res
        dist+=res
    print dist%1000000007