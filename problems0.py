import copy
cases = int(raw_input())
for c in range(cases):
    days = 0
    NK = raw_input().strip().split(" ")
    N = int(NK[0])
    K = int(NK[1])
    unsolved = map(int, raw_input().strip().split(" "))
    #print(unsolved)
    while unsolved != []:
        min = 0
        problems = copy.copy(unsolved)
        for pro in problems:
            #print([pro, min])
            if min==0 or (pro <= min-K or pro >= min+K):
                min = pro
                unsolved.remove(pro)
        days += 1
    print(days)
