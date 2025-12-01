def find_arr(arr, x):
    arr.sort()
    l = 0
    r = len(arr) - 1
    while l < r:
        m = int((l + r) / 2)
        if arr[m] == x:
            return True
        elif arr[m] < x:
            l = m + 1
        else:
            r = m -1
    return False

print(find_arr([1,2,-2,3,4], 3))
print(find_arr([1,-1,10,2,3], 5))