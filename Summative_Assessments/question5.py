def pairs(k, arr):
    arr.sort()
    num_pairs = 0
    for x in arr:
        if x + k in arr:
            num_pairs += 1
    return num_pairs

# Example
k = 1
arr = [1, 2, 3, 4]
num_pairs = pairs(k, arr)
print(num_pairs)  # 3
