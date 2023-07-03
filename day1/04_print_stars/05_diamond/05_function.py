def diamond(h):
    pivot = h // 2

    for i in range(h):
        if i <= pivot:
            print(f"{' ' * (pivot - i)}{'*' * (i * 2 + 1)}")
        else:
            print(f"{' ' * (i - pivot)}{'*' * ((h - i) * 2 - 1)}")

diamond(5)
diamond(7)
diamond(9)
