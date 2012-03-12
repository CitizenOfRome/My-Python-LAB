N = int(raw_input())
for n in xrange(N):
    db = {}
    query = raw_input().lower().split()
    if query[0]=="add":
        db[query[2]] = [query[1], query[3], query[4:]] 
    if query[0]=="del":
        del db[query[1]]
    if query[0]=="query":
        ret = []
        rappend = ret.append
        max = int(query[1])
        rlen = 0
        for k,v in db:
            if query[2:]==v[2]:
                rappend(k,v)
            if rlen==max: break
        