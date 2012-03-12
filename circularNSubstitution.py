import string
def circularNSubstitution(data, key):
    '''Returns the ROTn (like rot13) of the given data where n is the key'''
    chars = string.printable
    result=[]
    for i in data:
        index = string.find(chars, i)
        index += key
        while index > len(chars):
            index -= len(chars)
        result.append(chars[index])
    return str(result)
print circularNSubstitution("ABCD", 13)
print circularNSubstitution("ABCD", -13)