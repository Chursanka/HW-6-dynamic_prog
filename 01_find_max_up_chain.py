def find_max_up(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            dp[i] = dp[i-1] + 1
    return max(dp)
