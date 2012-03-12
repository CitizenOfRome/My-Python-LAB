import re
import sys
T = int(raw_input())
eids={}
adrs={}
ccs={}
#fraud = []
dic={"street": "st.", "road": "rd.", "illinois": "il", "california": "ca", "new york": "ny"}
plsch = ""
for i in xrange(T):
    (oid,did,eid,adr,cty,stt,zp,cc) = raw_input().split(",")
    if cc in ccs.itervalues():  continue
    #oid = int(oid)
    tadr = (adr+cty+stt).lower()+zp
    tadr = re.sub(r"(new\ york|street|california|road|illinois)", lambda m:dic[m.group()], tadr)
    eid=eid.replace(".", "").lower()
    try:
        eid=eid[:eid.index("+")]+eid[eid.index("@"):]
    except:pass
    teid = did+eid
    ttad = did+tadr
    n1=[key for key, value in eids.iteritems() if value == teid]
    if n1!=[]:
        #fraud += [n1[0], oid]
        sys.stdout.write(plsch+n1[0]+","+oid)
        plsch=","
    else:
        n2=[key for key, value in adrs.iteritems() if value == ttad]
        if n2!=[]:
            #fraud += [n2[0], oid]
            sys.stdout.write(plsch+n2[0]+","+oid)
            plsch=","
    ccs[oid] = cc
    eids[oid] = teid
    adrs[oid] = ttad

#print ",".join(map(str, fraud))