N = int(raw_input())
total = 0
total2 = 0
scores = []
scores2 = []
for n in xrange(N):
    [R,S] = map(float, raw_input().split())
    R=int(R)
    if R>n+1:
       k = R-1-n
       scr1 = (scores[-1]+S)/2
       scr2 = (scores2[-1]+S**2)/2
       scores += [scr1]*k
       scores2 += [scr2]*k
       total += scr1*k
       total2 += scr2*k
    total += S
    scores += [S]
    S2 = S**2
    total2+=S2
    scores2 += [S**2]

print [sum(scores[:n])/total for n in xrange(1,N+1)]
print [sum(scores2[:n])/total2 for n in xrange(1,N+1)]
