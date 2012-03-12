#from collections import Counter
T = int(raw_input())
l = set("HACKERCUP")
for t in xrange(1,T+1):
    line = filter(lambda x: x in l, raw_input())
    f = []
    fapp = f.append
    for i in l:
        c = line.count(i)
        if i=="c": k=2
        else:   k=1
        if c<k:
            print "Case #"+str(t)+": 0"
            break
        fapp(c/k)
    else:
        print "Case #"+str(t)+": "+str(min(f))