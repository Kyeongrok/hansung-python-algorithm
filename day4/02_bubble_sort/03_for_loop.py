arr = [7, 2, 3, 9, 28, 11]

for i in range(len(arr) - 1):
    # 2 --> i로 3 --> i + 1로
    if arr[i] > arr[i + 1]:
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
    print(arr)
