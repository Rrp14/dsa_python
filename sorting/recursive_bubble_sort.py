def rec_bubble(arr,n):

    if n==1:
        return arr

    did_swap=False

    for j in range(n-1):
        if arr[j] > arr[j + 1]:
           arr[j],arr[j+1]=arr[j+1],arr[j]
           did_swap=True


    if not did_swap:
        return arr

    rec_bubble(arr, n-1)

    return arr


print(rec_bubble([5,4,3,2,1],5))





