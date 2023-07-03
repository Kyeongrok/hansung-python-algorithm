h = 5
pivot = 5 // 2

for i in range(h):
    if i <= pivot:
        print(f"{' ' * (pivot - i)}{'*' * (i * 2 + 1)}")
    else:
        print(f"{' ' * (i - pivot)}{'*' * ((h - i) * 2 - 1)}")
