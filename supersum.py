def super_sum(arr):
    hash_map = {}
    for x in arr:
        if x in hash_map:
            hash_map[x] +=1
        else:
            hash_map[x] = 1

    keys = sorted(hash_map.keys())
    n = len(keys)

    if n == 1:
        return keys[0] * hash_map[keys[0]]

    dp = [0] * n
    dp[0] = keys[0] * hash_map[keys[0]]

    if keys[1] == keys[0] + 1:
        dp[1] = max(dp[0], keys[1] * hash_map[keys[1]])
    else:
        dp[1] = dp[0] + keys[1] * hash_map[keys[1]]

    for i in range(2, n):
        if keys[i] == keys[i - 1] + 1:
            dp[i] = max(dp[i - 1], dp[i - 2] + keys[i] * hash_map[keys[i]])
        else:
            dp[i] = dp[i - 1] + keys[i] * hash_map[keys[i]]

    return dp[-1] % ((10**9) +7)


# Example usage
arr = [1,2,3,3,3,4,4]
result = super_sum(arr)
print(f"Super Sum: {result}")  # Expected output: 4 (select keys 1 and 3)
