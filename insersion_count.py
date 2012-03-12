def intr(a, N):
    ret = N*(N-1)/2
    MAX = max(a)
    c = map(lambda x:0, xrange(MAX))
    for i in xrange(0, N):
        j = a[i]
        while j>0:
            ret -= c[j]
            j -= j & -j
        j = a[i]
        while j<MAX:
            c[j] += 1
            j += j & -j
    return ret

def sort(a, N):
    count = 0
    for i in xrange(1, N):
        j = i
        while j >= 1 and a[i] < a[j - 1]:   j -= 1
        count += i-j
        if j!= i:   a = a[:j]+[a[i]]+a[j:i]+a[i+1:]
    return count

no = int(raw_input())

for i in xrange(no):
    N = int(raw_input())
    a = map(int, raw_input().split(" "))
    print sort(a, N)
    # print intr(a, N)