def solution(N):
    bin_N = bin(N)[2:]
    cnt_of_0 = 0
    ans = 0
    for b in bin_N:
        if b == "0":
            cnt_of_0 += 1
        else:
            ans = max(ans, cnt_of_0)
            cnt_of_0 = 0
    return ans
