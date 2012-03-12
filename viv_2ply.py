from math import log
power_ones = [1] #Holds no of zeros in the series 0...i in each i

for i in range(32):
    power_ones.append(2 * power_ones[i] + 2 ** i - 1)

def count_pos(n):
    '''Isolate MSB and add the no of 1s in 10000...s to get total 1s in series 0...n'''
    if n == 0: return 0
    bits = int(log(n, 2))
    power = int(2 ** bits) #Num like 1000... <= n
    return power_ones[bits] + count_pos(n - power) + n - power
    #n-power=removing the MSB
def count_neg(n):
    '''If neg, count for 2's cpl of num + extra 1s'''
    if n == 0: return 0
    return 32 * n + count_pos(-n-1)

def count(a, b):
    if a > 0:
        return count_pos(b) - count_pos(a - 1)
    if b < 0:
        return count_neg(b + 1) - count_neg(a)
    if a == 0:
        return count_pos(b)
    if b == 0:
        return -count_neg(a)
    return count_pos(b) - count_neg(a)

T = int(raw_input())
for i in range(T):
    [A,B] = map(int, raw_input().split())
    print count(A, B)