

def merge(arr,low,mid,high):
    temp=[]
    left,right=low,mid+1


    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1

        else:
            temp.append(arr[right])
            right+=1

    while left<=mid:
        temp.append(arr[left])
        left+=1

    while right<=mid:
        temp.append(arr[right])
        right+=1


    for i in range(low,high+1):
        arr[i]=temp[i-low]


    print(temp)





def mergesort(arr,low,high):

    if low >=high:
        return
    mid=(low+high)//2

    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)



mergesort([5,4,3,2,1,0],0,5)