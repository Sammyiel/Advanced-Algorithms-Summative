def lilys_homework(arr):
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr1.sort()
    arr2.sort(reverse=True)
    swaps1 = 0
    swaps2 = 0
    for i in range(len(arr)):
        if arr1[i] != arr[i]:
            swaps1 += 1
        if arr2[i] != arr[i]:
            swaps2 += 1
    return min(swaps1, swaps2)

# Example
arr = [7, 15, 12, 3]
num_swaps = lilys_homework(arr)
print(num_swaps)  # 3
