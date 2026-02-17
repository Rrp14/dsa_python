"""using min indicator"""
def find_smallest(arr):

    if len(arr)<1:
        return arr[0]

    minimum=arr[0]

    for i in range(1,len(arr)-1):
        if arr[i]<minimum:
            minimum=arr[i]

    return minimum


print(find_smallest([3,4,5,2,3,5,67,4,3]))

"""using sorting"""

def find_smallest_sort(arr):

    #sorted(arr)
    arr.sort()

    return arr[0]

print(find_smallest_sort([5,6,7,8,4,3,2,1,45]))

