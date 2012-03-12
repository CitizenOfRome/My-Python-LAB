import itertools
N = int(raw_input())
V = []
sets = itertools.permutations(xrange(N))
for i in xrange(N):
    V.append(map(int, raw_input().split()))

def get_sum(set, V, N):
    '''Returns the required sum'''
    sum = 0
    for i in xrange(N-1):
        sum+=V[set[i]][set[i+1]]
    return sum

max = 0
res = None
for set in sets:
    try:
        val=get_sum(set, V, N)
        if val>max:
            res = set
            max = val
    except: break
print " ".join(map(str, res))
