def dis_1(a, b):
    return len(filter(bool,[x in b for x in a]))==1
    
def score(s):
    d = {'A':1, 'E':1, 'I':1, 'L':1, 'N':1, 'O':1, 'R':1, 'S':1, 'T':1, 'U':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10}
    return sum([d[x] for x in s])

L = int(raw_input())
N = int(raw_input())
db = {}
for n in xrange(N):
    st = raw_input().upper()
    if len(st)!=L: continue
    db[st]=score(st)
print db
