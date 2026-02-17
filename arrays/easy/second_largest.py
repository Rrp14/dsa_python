"""better approach to get T,S=O(n) and O(1)"""
def find_second_largest(arr):

    if len(arr)==0 or len(arr)==1:
        print(-1)
        return

    large=float("-inf")
    second_large=float('-inf')


    for i in range(len(arr)):

        large=max(large,arr[i])

        if arr[i]>second_large and arr[i]!=large:
            second_large=arr[i]


    print(second_large)


find_second_largest([3,5,6,7,9,1,8])


"""brute force O(nlogn) and O(1)"""

def find_second_largest_bf(arr):
    n=len(arr)

    if n==0 or n==1:
        print(-1)
        return

    arr.sort()

    print(arr[n-2])

find_second_largest_bf([3,5,6,7,9,1,8])








