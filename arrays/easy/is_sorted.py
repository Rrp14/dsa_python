def find_is_sorted(arr):
    n=len(arr)

    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True




print(find_is_sorted([2,1,3,4]))
print(find_is_sorted([1,2,3,4,5]))
