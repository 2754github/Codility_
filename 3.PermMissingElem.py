def solution(A):
    n = len(A)+1
    return int(0.5*n*(n+1)-sum(A))
