# from itertools import permutations
# def combo(N, M, D):
    # for com in combinations(xrange(1,N+1), M):
        # breakout = False
        # com = list(com)
        # print com
        # if com.reverse()==com:  pal = 1
        # else: pal = 2
        # for x in com:
            # if breakout: break
            # for y in com[1:]:
                # if not(y==x and -D<=y-x<=D):
                    # breakout = True
                    # break
            # else:
                # yield pal
        #if [y!=x and -D<=y-x<=D for x in com for y in com[1:]]
def sections(seq, mx, ln):
    for q in xrange(2, mx+1):
        w = 0
        while w+q<=ln:
            yield seq[w:w+q]
            w += 1
def get_runs(seq, mx):
    pass
def sm(seq, D):
    db = [0]+[1]*N
    for m, k in enumerate(seq):
        for n in xrange(1, m):
            if m!=n and -D<=db[m]-db[n]<=D:
                db[m] += db[n]
    return sum(db)-1
T = int(raw_input())
for t in xrange(T):
    [N,M,S,D] = [int(x) for x in raw_input().split()]
    # i = 0
    # for z in combo(N,M,D):
        # i+=z
    seq = (range(1, S+1)*2)
    i = 0
    for pe in sections(seq, N, len(seq)):
        print pe, sm(pe, D)
        if sm(pe, D)==M:    i+=1
    print i%1000000007