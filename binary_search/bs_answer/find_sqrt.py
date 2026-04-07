def find_sqrt(v):

    left,right=0,v-1

    while left <= right:

        mid=(left+right)//2

        if mid**2<=v:
            return mid

        elif mid**2>v:
            right=mid-1

        else:
            left=mid+1



    return None


res=find_sqrt(36)
print(res)


