#python 2.7.2
T = int(raw_input())
for t in xrange(1,T+1):
    [N, P, W, M, K, A, B, C, D] = map(int, raw_input().split())
    lst = [[W,P]]
    i = 1
    while i<N:
        W = ((C*W+D)%K)+1
        P = ((A*P+B)%M)+1
        I = [W, P]
        if I in lst:    break
        lst+=[I]
        i+=1
    #print lst
    wc = 0
    bc = 0
    ll = len(lst)
    #print lst
    nll = N/ll
    ns = N-nll*ll
    #print N, ll, nll, ns
    for itm in lst:
        b = True
        w = True
        for it2 in lst:
            if b and ((itm[0]<=it2[0] and itm[1]<it2[1]) or (itm[0]<it2[0] and itm[1]<=it2[1])):
                #print "b", "".join(map(str,itm)), "".join(map(str,it2))
                b = False
            if w and ((itm[0]>=it2[0] and itm[1]>it2[1]) or (itm[0]>it2[0] and itm[1]>=it2[1])):
                #print "w", "".join(map(str,itm)), "".join(map(str,it2))
                w = False
            if not (b or w): break
        #else:   print "el", "".join(map(str,itm)), "".join(map(str,it2))
        if b:   bc+=nll
        if w:   wc+=nll
    if ns>0:
        for itm in lst[:ns]:
            b = True
            w = True
            for it2 in lst:
                if b and ((itm[0]<=it2[0] and itm[1]<it2[1]) or (itm[0]<it2[0] and itm[1]<=it2[1])):
                    #print "bs", "".join(map(str,itm)), "".join(map(str,it2))
                    b = False
                if w and ((itm[0]>=it2[0] and itm[1]>it2[1]) or (itm[0]>it2[0] and itm[1]>=it2[1])):
                    #print "ws", "".join(map(str,itm)), "".join(map(str,it2))
                    w = False
                if not (b or w): break
            if b:   bc+=1
            if w:   wc+=1
        #print "".join(map(str,itm)), str(bc), str(wc)
    print "Case #"+str(t)+": "+str((bc))+" "+str((wc))
