arr = [7, 2, 3, 9, 28, 11]

temp = arr[0]
arr[0] = arr[1]
arr[1] = temp

for i in range(len(arr)):
    print(arr[i])