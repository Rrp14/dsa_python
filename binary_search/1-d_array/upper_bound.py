def upperBound(nums,left,right,target):
    if left>right:
        return left
    mid=(left+right)//2

    if nums[mid]>target:
        return upperBound(nums,left,mid-1,target)
    else:
        return upperBound(nums,mid+1,right,target)



res=upperBound([1,2,2,3],0,3,2)
print(res)

