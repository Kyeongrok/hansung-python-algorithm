
def print_1_to_100(n):
    if n > 100:
        return
    print(n)
    print_1_to_100(n + 1)

print_1_to_100(1)