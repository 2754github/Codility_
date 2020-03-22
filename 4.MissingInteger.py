def solution(A):
    ans = 1
    B = list(set(sorted(A)))
    for i, b in enumerate(B):
        if i + 1 == b:
            pass
        else:
            ans = i+1
            break
    else:
        ans = len(B)+1
    return ans
