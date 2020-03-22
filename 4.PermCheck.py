def solution(A):
    n = len(A)
    B = list(range(1, n + 1))
    l = len(B)
    for a in A:
        if a - 1 < l:
            B[a - 1] = 0
        else:
            break
    return int(B.count(0) == l)
