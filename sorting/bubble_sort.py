def bubble_sort(arr):
    n=len(arr)
    is_swap=False

    for i in range(n-1,0,-1):

        for j in range(0,i):

            if arr[j]>arr[j+1]:

                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                is_swap=True

                """check is to convert brute force to optimal and avoid worst case"""
        if not is_swap:
                print(arr)
                return





    print(arr)


bubble_sort([5,2,3,4,1])