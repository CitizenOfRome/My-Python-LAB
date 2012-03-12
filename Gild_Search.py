import sys
file = open(sys.argv[1], "r")
db = {}
for line in file:
    item = line.split("=")[-1][:-2]
    if item not in db:  db[item] = 1
    else:   db[item] += 1
result = map(lambda (k,v):(k), sorted(db.iteritems(), key=lambda (k,v): (v,k))[-5:])
for i in xrange(1,6):
    print(result[-i])