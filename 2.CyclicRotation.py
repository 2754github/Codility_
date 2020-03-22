def solution(A, K):
    l = len(A)
    if l == 0:
        return []
    else:
        K %= l
        A.extend(A)
        return A[l-K:2*l-K]
