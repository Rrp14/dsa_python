def lowerBound(nums,left,right,target):
    if left>right:
        return left
    mid=(left+right)//2

    if nums[mid]>=target:
        return lowerBound(nums,left,mid-1,target)
    else:
        return lowerBound(nums,mid+1,right,target)



res=lowerBound([1,2,2,3],0,3,2)
print(res)

