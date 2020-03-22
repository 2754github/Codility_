def solution(A, K):
    l = len(A)
    K %= l
    A.extend(A)
    return A[l-K:2*l-K]
