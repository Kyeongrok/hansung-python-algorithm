h = 5
pivot = 5 // 2

for i in range(h):
    if i <= pivot:
        print(f"{' ' * (h - i - 1)}{'*' * (i * 2 + 1)}")
    else:
        print(i, 'reverse')
