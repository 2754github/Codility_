def solution(A):
    l = A[0]
    r = sum(A) - l
    ans = abs(l-r)
    for i in range(1, len(A) - 1):
        l += A[i]
        r -= A[i]
        ans = min(ans, abs(l-r))
    return ans
