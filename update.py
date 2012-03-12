def findChanges(cStr, pStr):
    '''Returns the start & end positions of change in a given pair of strings'''
    pLen = len(pStr)
    cLen = len(cStr)
    for i in range(pLen):
        if cStr[i] != pStr[i]:
            start = i
            break
    else:
        start = pLen
    for i in range(pLen):
        if cStr[cLen-1-i] != pStr[pLen-1-i]:
            end = pLen-i
            cEnd = cLen - i
            break
    else:
        end = 0
        cEnd = cLen - pLen
    data = cStr[start:cEnd]
    return [start, end, data]

def update(pStr, start, end, data):
    '''Returns the updated form of the given string with the given data inserted between the given indices'''
    return pStr[0:start] + data + pStr[end:len(pStr)]

pDat = "abcd"
cDat = "abcd234abc6d"
chx = findChanges(cDat, pDat)
print chx
print update(pDat, chx[0], chx[1], chx[2])

# Dynamic errors : Can dynamic adjustment be done, with the update func?
# 1. Parallel edits - With updates being based on an older pStr
#     Each pStr gets a ref-id & the update must be re-adjusted to newer ones, as needed
# 2. Message order errors - Again, edit happens over the wrong pStr
#     Wait for the right ref num?
#     Adjust for the unreceieved messeges? - adjust with spaces is error prone as pos is unknown
