def find_missing(arr):
    n=len(arr)+1
    total=sum(arr)

    exp_total=(n*(n+1))/2

    return int(exp_total-total)


res=find_missing([1,4,5,3])
print(res)


def find_missing_ls(arr):
    

    n=len(arr)+1
    for i in range(1,n+1):
        found=False

        for j in range(n-1):
            if arr[j]==i:
                found=True
                break



        if not found:
         return i

    return -1

print(find_missing_ls([1,3,4,5]))


