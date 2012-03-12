import copy

def act(st):
    '''Return the list of possible end-combos'''
    final = []
    fappend = final.append
    lmd = lambda i: (st[i]==st[i+1]) and -1 or i
    chk = lambda x: x>=0
    rs = [[st, filter(chk, map(lmd, xrange(len(st)-1)))]]
    if rs[0][1]==[]and st not in final:  final = [st]
    else:
        next = copy.copy(rs)
        while next!=[]:
            rs = copy.copy(next)
            next = []
            nxtnd = next.extend
            for stuff in rs:
                st = stuff[0]
                for i in stuff[1]:
                    if (st[i]=="a" and st[i+1]=="b") or (st[i]=="b" and st[i+1]=="a"):   item = (st[:i]+"c"+st[i+2:])
                    elif (st[i]=="c" and st[i+1]=="b") or (st[i]=="b" and st[i+1]=="c"): item = (st[:i]+"a"+st[i+2:])
                    elif (st[i]=="c" and st[i+1]=="a") or (st[i]=="a" and st[i+1]=="c"): item = (st[:i]+"b"+st[i+2:])
                    else:   continue
                    stk = [[item, filter(chk, map((lambda i: (item[i]==item[i+1]) and -1 or i), xrange(len(item)-1)))]]
                    if stk[0][1]==[] and (item not in final):
                        fappend(item)
                    else:
                        nxtnd(stk)
    return final

def split(st, const=5, cbak=act):
    '''Splits st into smaller chunks and returns a 2D tuple of their result from the given call-back'''
    lst = len(st)
    result = []
    rappend = result.append
    i=0
    while i<lst:
        ret = cbak(st[i:i+const])
        #print([const, ret])
        j=-1
        de = 0
        while j<=1 and len(ret)==1 and ret[0]==st[i:i+const+de]:
            ret = cbak(st[i:i+const+j])
            de = j
            j += 1
        print(i, i+const+de, const, j, ret, ret[0]==st[i:i+const+de])
        rappend(ret)
        i += const + de
    #print(["sp", const, st, result])
    return result

def mix(result):
    '''Combines the split strings and returns a list of combined strings'''
    skt = []
    sappend = skt.append
    tot = map(lambda x:(len(x)-1), result)
    lst = map(lambda x:0, tot) #Truth-table approach
    ll = len(lst)
    totp = copy.deepcopy(tot)
    totp[-1]+=1
    while lst!=totp:
        k=1
        while k<=ll and lst[-k] > tot[-k]:
            lst[-k] = 0
            if k+1<=ll: lst[-(k+1)] += 1
            k += 1
        j = 0
        res = ""
        for i in lst:
            res += result[j][i]
            j += 1
        sappend(res)
        lst[-1] += 1
    return skt

def do_big(st, const=5, cbak=act):
    '''Get the end-cases for a large string using the split-mix combo'''
    ls = [st]
    lx = ls.extend
    le = lambda x: lx(filter(bool,map((lambda y:y not in ls and y), x)))
    res = []
    ra = res.append
    for it in ls:
        rs = split(it, const, cbak)
        if it == rs[0][0]:
            ra(it)
            continue
        mx = mix(rs)
        # if mx[0]==it:   map(ra, do_big(it, const+1))
        # else:   
        le(mx)
        #print([it == rs[0][0], it, rs, mx])
    if res==[]: res=[st]
    print(const, res)
    return res

no = int(raw_input())
#cache = {}

for i in xrange(no):
    st = raw_input()
    print(min(map(len, do_big(st, 25, do_big))))
