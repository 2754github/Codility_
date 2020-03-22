def solution(A):
    n = len(A)
    return int(0.5*n*(n+1) == sum(A))
