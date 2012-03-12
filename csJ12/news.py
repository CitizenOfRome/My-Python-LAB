import json
import string
from collections import Counter
#import heapq
objs = raw_input().lower()
common = ["the", "a", "it", "its", "of", "are", "is", "that", "this", "to", "as", "have", "has", "had", "will", "not", "wont", "in", "and", "for", "on", "while", "would", "each", "can", "more", "with", "about", "they", "said", "also", "at", "their", "if", "be", "what", "were", "been", "but", "from", "was", "did", "by", "them", "our", "could", "where", "you", "how", "which", "well", "just", "show", "even", "an", "than", "or", "so", "now", "able", "into", "much", "some", "she", "he", "we", "do", "look", "see", "who", "body", "surface", "like", "up", "all", "help", ""]
objs = json.loads(objs)
out = {}
pairs = []
pappend = pairs.append
for obj in objs:
    c = Counter(map(lambda x:x[-1]=="s" and x[:-1] or x, filter(lambda x: x not in common, str((obj["title"]+" ")*4+obj["content"]).replace("\n", " ").replace("'s", "").translate(string.maketrans("",""), string.punctuation).split(" "))))
    k = [key for key, value in out.iteritems() if len(value&c)>=(len(c)*0.25)]
    oid = obj["id"]
    out[oid] = c
    for i in xrange(len(pairs)):
        if [i for j in k if j in pairs[i]]!=[]:
            pairs[i].append(oid)
            break
    else:
        pappend(k+[oid])
    #print c
    # print [key for key, value in c.iteritems() if value>2]
    # print heapq.nlargest(10, c, key=c.get)
# print out
print pairs