def fib(n):
    dp = [None] * n
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    # print(dp)
    return dp[n - 1]

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

from datetime import datetime

n = 37
print(datetime.now())
print(fib_recursive(n))
print(datetime.now())
print(fib(n))
print(datetime.now())
