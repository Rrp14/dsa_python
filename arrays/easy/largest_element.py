"""using max indicator"""
def find_largest(arr):

    if len(arr)<1:
        return arr[0]

    maximum=arr[0]

    for i in range(1,len(arr)-1):
        if arr[i]>maximum:
            maximum=arr[i]

    return maximum


print(find_largest([3,4,5,2,3,5,67,4,3]))

"""using sorting"""

def find_largest_sort(arr):

    #sorted(arr)
    arr.sort()

    return arr[-1]

print(find_largest_sort([5,6,7,8,4,3,2,1,45]))

