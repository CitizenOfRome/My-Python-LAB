#!/usr/bin/python
'''A filltool program which takes a file-name containig a b/w pixel array & gives the number of transforms required to convert all the whites to blacks: for a better explanation refer to http://www.gild.com/challenges/details/295'''
#Author: Sathvik Ponangi (psathvik@gmail.com)
#Licence, if applicable: http://creativecommons.org/licenses/by-sa/3.0/
# write here your solution for filltool using Python 

import sys
import copy

def str2arr(s):
    '''String to list of its characters'''
    lst = [s[i] for i in xrange(len(s))]
    # for i in range(len(s)):
        # lst.append(s[i])
    return lst

def print_arr(l):
    '''Prints the items in an array, seperating them by a new line'''
    for i in l:
        print(i)
    print("")

def infect(x, y):
    '''Infects everything it can : Changes black to white in contigious locations'''
    global pic, H, W
    lH = H
    lW = W
    lpic = pic
    lpic[x][y] = "1"
    stack = []
    range_x = xrange(max(0,x-1), min(lH,x+2))
    range_y = xrange(max(0,y-1), min(lW,y+2))
    append = stack.append
    for i in range_x:
        for j in range_y:
            if lpic[i][j]=="0":
                lpic[i][j] = "1"
                append([i, j])
    # fn = lambda i,j: ([i,j]) if lpic[i][j]=="0" and lpic[i][j]="1" #Assignments are illegal
    # stack = [fn(i,j) for i in range_x for j in range_y]
    # itr = lambda m,n: ((lpic[m][n]=="0")) and lpic[m][n]="1" and append([m, n])
    # map(itr, range_x, range_y)
    pic = lpic
    return stack

def callout(lst):
    '''A dummy function, used with loops to workaround max recursion errors: Not usually required'''
    stack = []
    extend = stack.extend
    itr = lambda x: extend(infect(x[0], x[1]))
    map(itr, lst)
    return stack

pic = [] #The picture matrix
file = open(sys.argv[1], "r")
H=0
W=0
for line in file:
    #print(line)
    if line=="": continue;
    if H==0:
        #For the first line
        HW = line.strip().split(" ")
        H = int(HW[0])
        W = int(HW[1])
        continue;
    pic.append(str2arr(line.strip()))

#old_pic = copy.deepcopy(pic) #Deepcopy is required to prevent copying of the reference
# full = copy.deepcopy(pic)
# for i in range(H):
    # for j in range(W):
        #The list thaat holds the final pic
        # full[i][j]="1"
full = map((lambda i:map(lambda j:1, xrange(W))), xrange(H))
count = 0
cache = xrange(H)
#print_arr(pic)
while pic!=full:
    #done = False
    #print(count)
    for i in cache:
        #if done: break
        try:    j = pic[i].index("0")
        except:
            try:    cache.remove(i)
            except: pass
            continue
        if pic[i][j]=="0":
            stack = infect(i, j)
            while stack!=[]:
                stack = callout(stack)
                #print(old_pic)
            #done = True
            count += 1
            #print_arr(pic)
            #old_pic = copy.deepcopy(pic)
            break
print(count)
file.close()

#This was fun & I can't wait for my iPad. Feel free to contact me for any clarifications :)