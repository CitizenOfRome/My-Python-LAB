def zero(m,n):
   return [[0 for row in xrange(n)] for col in xrange(m)]

def mul(matrix1,matrix2):
    new_matrix = zero(len(matrix1),len(matrix2[0]))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        if new_matrix[i][j]!=0: new_matrix[i][j] = 1
    return new_matrix

T = int(raw_input())
for t in xrange(T):
    raw_input()
    N = int(raw_input())
    A = []
    B = []
    C = []
    for n in xrange(N):
        A.append([int(x) for x in raw_input().split()])
    raw_input()
    for n in xrange(N):
        B.append([int(x) for x in raw_input().split()])
    raw_input()
    for n in xrange(N):
        C.append([int(x) for x in raw_input().split()])
    D = zero(len(A),len(B[0]))
    # for i in xrange(len(A)):
        # for j in xrange(len(B[0])):
            # for k in xrange(len(B)):
                # D[i][j] += A[i][k]*B[k][j]
        # if D[i][j]!=0: D[i][j] = 1
        # if D[i][j]!=C[i][j]:
            # print "no"
            # break
        # else: print D[i][j],
    # else:
        # print "yes"
    if mul(A,B)==C: print "yes"
    else:   print "no"