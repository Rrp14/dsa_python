def rec_insertion(arr,n,i):

    if i==n:
        return arr

    j=i


    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1


    rec_insertion(arr,n,i+1)

    return arr





print(rec_insertion([5,4,3,2,1],5,0))


