T = int(raw_input())

for i in xrange(T):
    [N,M] = map(int, raw_input().split())
    K = N-M
    print  str((2**(M+1))*((2**K)-1))+".00"
    
# 300 199
# 999 127
