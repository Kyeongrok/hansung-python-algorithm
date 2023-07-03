def print_pyramid(h):
    for i in range(h):
        print(f"{' ' * (h - i - 1)}{'*' * (i * 2 + 1)}")

print_pyramid(3)
print_pyramid(4)
