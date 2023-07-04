def factor(num):
    for i in range(1, num + 1):
        remainder = num % i
        if remainder == 0:
            print(i, end=' ')

factor(6)