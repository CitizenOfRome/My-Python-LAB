T = int(raw_input())
for t in xrange(T):
    line = raw_input().split()
    H = int(line[0])
    W = int(line[1])
    line = line[2:]
    lens = map(len, line)
    biggest = max(lens)
    