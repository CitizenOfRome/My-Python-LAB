'''Issue:Memory'''
import itertools
C = int(raw_input())
for c in xrange(C):
    [N,T,M] = map(int, raw_input().split())
    T+=1
    conn=[[i] for i in xrange(N)]
    for i in xrange(M):
        [v1,v2]=map(lambda x:int(x)-1, raw_input().split())
        conn[v1]+=[v2]
        conn[v2]+=[v1]
    nc = []
    nxtend = nc.extend
    conn=filter(bool, [set(x) if len(x)<=T else nxtend(list(itertools.combinations(x, T))) for x in conn])
    conn+=[set(x) for x in nc]
    nc, nxtend = None, None
    #print conn
    conn_len = map(len, conn)
    conn_rng = xrange(len(conn))
    print max(map(lambda y:max([conn_len[x]+conn_len[y] for x in conn_rng if conn[x]&conn[y]==set()]+[0]), conn_rng))