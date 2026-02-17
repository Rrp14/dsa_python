def second_smallest_bf(arr):
    n=len(arr)

    if n==0 or n==1:
        return

    arr.sort()

    return arr[1]

print(second_smallest_bf([3,4,5,2,1,3,4,6]))


def second_smallest_op(arr):
    n=len(arr)

    if n==0 or n==1:
        return

    smallest=float("inf")
    second_smallest=float("inf")

    for i in range(n):

        if arr[i]<smallest:
            second_smallest=smallest
            smallest=arr[i]

        elif arr[i]<second_smallest and  arr[i]!=smallest:
            second_smallest=arr[i]

    return second_smallest

print(second_smallest_op([4,5,6,3,2,1,4,5,6]))

