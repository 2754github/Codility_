def solution(N, A):
    Cntr = [0]*N
    for a in A:
        if a == N+1:
            Cntr = [max(Cntr)]*N
        else:
            Cntr[a-1] += 1
    return Cntr
