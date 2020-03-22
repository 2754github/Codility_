def solution(A):
    B = [0]*(10**6)
    l = len(B)
    for a in A:
        if 0 <= a - 1 < l:
            B[a - 1] = a
    return B.index(0)+1
