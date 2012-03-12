import re
C = int(raw_input())
for c in xrange(C):
    [R,N]=raw_input().split()
    N = int(N)
    print re.findall(r"\((.*)\)", R[1:-1])