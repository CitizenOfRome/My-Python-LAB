#Do as many probs as you can, in a day
import copy
cases = int(raw_input())
def itr(lst):
    '''Gives the best of possible problems you can solve form the list of items'''
    global unsolved, K, cache, uno
    k = K
    problems = unsolved
    cases = []
    #print(lst)
    for item in lst:
        if item==[]: continue
        solns = []
        base = item[0]
        index = item[1]
        if cache[index] != []:
            cases.append(cache[index])
        else:
            i = index+1
            pros = problems[i:]
            for pro in pros:
                if (pro <= base-k or pro >= base+k):
                    solns.append([pro, i])
                i += 1
            #print(["solns:", solns])
            #print(["item", item])
            if solns==[]:
                cases.append([[item], 1])
                uno.append([[item], 1])
            else:
                res = itr(solns)
                #print(["[item]", [item], "res0", res[0], "ext", [item]+(res[0])])
                cases.append([[item]+res[0], res[1]+1])
            cache[index] = cases[len(cases)-1]
    prev = 0
    best = None
    #print(["cases", cases])
    for case in cases:
        #print(case)
        if case[1] > prev:
            best = case
            prev = case[1]
    #print([lst, best])
    return best
for c in range(cases):
    days = 0
    NK = raw_input().strip().split(" ")
    N = int(NK[0])
    K = int(NK[1])
    unsolved = map(int, raw_input().strip().split(" "))
    while unsolved != []:
        #print("----------------")
        arr = map((lambda x:[x,unsolved.index(x)]), unsolved)
        cache = map((lambda x: []), unsolved)
        uno = [] #Holds dead-ends
        #print(arr)
        today = itr(arr)
        #print(today)
        map((lambda obj:unsolved.remove(obj[0])), today[0])
        for obj in uno:
            try:
                unsolved.remove(obj[0])
                days += 1
            except: pass
        days += 1
    print(days)