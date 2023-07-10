def fib(n):
    dp = [None] * n
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp)
    return dp[n - 1]

print(fib(5))
print(fib(8))
