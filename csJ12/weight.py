'''Fix for non seq sub seqs'''
C = int(raw_input())
for c in xrange(C):
    N = int(raw_input())
    A = map(int, raw_input().split())
    W = map(int, raw_input().split())
    ops = [0]
    oapp = ops.append
    #print A,W
    for i in xrange(N):
        #[W[x] for x in xrange(i+1:N) A[x]>A[i]]
        try:
            if A[i]<A[A.index(A[i]+1)]:
                ops[-1]+=W[i]
                #print i,
            else:
                ops[-1]+=W[i]
                oapp(0)
                #print i
        except:
            ops[-1]+=W[i]
            oapp(0)
            #print i
    #print (ops)
    print max(ops)
    