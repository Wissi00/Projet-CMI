def w1(A,B,C,P):
    return (A[0]*(C[1]-A[1])+(P[1]-A[1])*(C[0]-A[0])-P[0]*(C[1]-A[1]))/((B[1]-A[1])*(C[0]-A[0])-(B[0]-A[0])*(C[1]-A[1]))

def w2(A,B,C,P):
    if C[1]-A[1]==0:
        return (P[1]-A[1]-w1(A,B,C,P)*(B[1]-A[1]))
    else:
        return (P[1]-A[1]-w1(A,B,C,P)*(B[1]-A[1]))/(C[1]-A[1])

def inTriangle(A,B,C,P):
    return (w1(A,B,C,P)>=0 and w2(A,B,C,P)>=0 and w1(A,B,C,P)+w2(A,B,C,P)<=1)
