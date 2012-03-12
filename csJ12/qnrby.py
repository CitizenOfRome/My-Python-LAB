[T, Q, N] = map(int, raw_input().split())
topics = {}
for i in xrange(T):
    [tid, lat, lng] = map(float, raw_input().split())
    topics[int(tid)] = [lat, lng]

questions = {}
for i in xrange(Q):
    seti = map(int, raw_input().split())
    if len(seti)<3: continue
    questions[seti[0]] = seti[2:]

def get_dist(A, B):
    '''Get ~ distance between two coods'''
    return (abs(B[0]-A[0])+abs(B[1]-A[1]))
    
for i in xrange(N):
    terms = raw_input().split()
    char=terms[0]
    max_results = int(terms[1])
    [lat, lng] = map(float, terms[2:])
    if char=="t":
        # dists = {}
        # for topic in topics:
            # dists[topic] = get_dist(topics[topic], [lat,lng])
        dists=dict(zip(topics.iterkeys(), [get_dist(topics[topic], [lat,lng]) for topic in topics]))
        print " ".join(map(lambda (k,v):str(k),sorted(dists.iteritems(), key=lambda (k,v):(v,-k))[:max_results]))
    else:
        dists = {}
        for question in questions:
            dds = None
            list = questions[question]
            for topic in list:
                val = get_dist(topics[topic], [lat,lng])
                if dds is not None: dds = min(dds, val)
                else: dds = val
            dists[question] = dds
        print " ".join(map(lambda (k,v):str(k), sorted(dists.iteritems(), key=lambda (k,v):(v,-k))[:max_results]))
        