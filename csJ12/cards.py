import itertools
T = int(raw_input())

for i in xrange(T):
    N = int(raw_input())
    M = map(int, raw_input().split())
    rng = xrange(len(M))
    combos = filter(lambda lst:[1 for j in rng if lst[j]>=j+1]==[], itertools.permutations(M))
    count=len(combos)
    print count%1000000007