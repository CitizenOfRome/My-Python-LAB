#Calc days for every possible case and pick the best of them
import copy
# import sys
# sys.setrecursionlimit(999999)
cases = int(raw_input())
def get_posby(lst):
    '''Gives a matrix with possible problems to tackle next for every index'''
    global unsolved, K, cache, uno
    k = K
    problems = unsolved
    cases = []
    for item in lst:
        if item==[]: continue
        solns = []
        base = item[0]
        index = item[1]
        i = index+1
        pros = problems[i:]
        for pro in pros:
            if (pro <= base-k or pro >= base+k):
                solns.append([pro, i])
            i += 1
        cases.append(solns)
    return cases
def call_it_a_day(stack):
    '''Whew, lets check out all that we've solved today'''
    global days, dead, arr
    l = len(days)
    if len(dead) < 1:   days.append(1)
    else:   days[l-1] += 1
    dead = dead+stack
    print([days, "day_ends", dead])
    if len(arr)==len(dead):
        '''End of days'''
        print([days, "end", dead])
        dead = []
    else:   rep(arr, [])
def rep(lst, stack=[]):
    '''Looking through every posssibility'''
    global posby, dead, arr
    #orig = copy.deepcopy(stack)
    if lst==[]: return call_it_a_day(stack)
    #if len(arr)==len(stack): return rep([], stack)
    for item in lst:
        if len(arr)==len(dead): return True #To prevent calls of the dead
        if len(arr)==len(stack): return True #To prevent calls of the dead
        if item == []: continue
        if item in dead: #Can't call it a day
            #print([item, "dead", dead])
            continue
        if not item in stack:   stack.append(item)
        nxt = posby[item[1]]
        nxt = filter(None,map((lambda x: x not in dead and x or None), nxt))
        print([item, nxt, stack])
        rep(nxt, stack)
        #stack = copy.deepcopy(orig)
for c in range(cases):
    days = []
    NK = raw_input().strip().split(" ")
    N = int(NK[0])
    K = int(NK[1])
    unsolved = map(int, raw_input().strip().split(" "))
    arr = map((lambda x:[x,unsolved.index(x)]), unsolved)
    posby = get_posby(arr)
    #print(arr)
    dead = []
    rep(arr)
    print(days)
    ldays = len(days) - 1
    if ldays<1: ldays=1
    print(min(days[:ldays]))