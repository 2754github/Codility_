def solution(A):
    ans = 0
    for a in A:
        ans ^= a
    return ans
