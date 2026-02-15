def selection_sort(arr):
    n=len(arr)


    for i in range(0,n):
        mini=i

        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j

        temp=arr[mini]
        arr[mini]=arr[i]
        arr[i]=temp

    print(arr)


selection_sort([5,4,3,2,1])

