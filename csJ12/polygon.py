def side(P0, P1, P2):
    #return (((P1["x"] - P0["x"])*(P2["y"]-P0["y"])) - ((P2["x"]-P0["x"])*(P1["y"]-P0["y"])))
    return P1["x"]*P2["y"]-(P0["x"]*(P2["y"]-P1["y"])+P0["y"]*(P1["x"]-P2["x"]))
def inn0(P, V, N):
    '''Winding Number Inclusion Algorithm: http://softsurfer.com/Archive/algorithm_0103/algorithm_0103.htm'''
    wn = 0
    for i in xrange(N-1):
        s = side(V[i], V[i+1], P)
        if s==0:
            return True
        if V[i]["y"]<=P["y"]:
            if V[i+1]["y"]>P["y"]:
                if s>0:
                    wn+=1
        else:
            if V[i+1]["y"]<=P["y"]:
                if s<0:
                    wn-=1
    return wn!=0
# def inn1(P, V, N):
    # cn = 0; 
    # for i in xrange(N-1):
       # if side(V[i], V[i+1], P)==0:
           # return True
       # if (((V[i]["y"] <= P["y"]) and (V[i+1]["y"] > P["y"])) or ((V[i]["y"] > P["y"]) and (V[i+1]["y"] <= P["y"]))):
            # vt = 1.0*(P["y"] - V[i]["y"]) / (V[i+1]["y"] - V[i]["y"])
            # if (P["x"] < V[i]["x"] + vt * (V[i+1]["x"] - V[i]["x"])):
                # cn+=1
    # return (cn&1)==1;
# def inn3(P,V,N):
    # i,j,c = 0,N-1,0
    # [testx,testy]=[P["x"], P["y"]]
    # while i < N:
        # if i<N-1 and side(V[i], V[i+1], P)==0:
            # return True
        # if ( ((V[i]["y"]>testy) != (V[j]["y"]>testy)) and (testx < (V[j]["x"]-V[i]["x"]) * (testy-V[i]["y"]) / (V[j]["y"]-V[i]["y"]) + V[i]["x"]) ):
            # c = ~c
        # j = i
        # i += 1
    # return c
[N, Q] = map(int, raw_input().split())
P = []
# Pappend = P.append
for i in xrange(N):
    [x,y] = map(int, raw_input().split())
    P+=[dict(x=x, y=y)]

for i in xrange(Q):
    M = int(raw_input())
    V = []
    # Vappend = V.append
    xmin,xmax,ymin,ymax=0,0,0,0
    for j in xrange(M):
        [x,y] = map(int, raw_input().split())
        if x<xmin:xmin = x
        if y<ymin:ymin = y
        if x>xmax:xmax = x
        if y>ymax:ymax = y
        V+=[dict(x=x, y=y)]
    count = 0
    for p in P:
        if (p["x"] < xmin or p["x"] > xmax or p["y"] < ymin or p["y"] > ymax): continue
        if inn0(p, V, M):    count+=1
    print count