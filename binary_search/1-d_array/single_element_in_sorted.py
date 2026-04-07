from typing import List


def singleNonDuplicate(nums:List[int])->int:

    n=len(nums)
    if n==1:
        return nums[0]

    if nums[0]!=nums[1]:
        return nums[0]

    if nums[n-1]!=nums[n-2]:
        return nums[n-1]




    left=1
    right=n-2

    while left<=right:

        mid=(left+right)//2

        if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
            return nums[mid]

        if (mid%2==0 and nums[mid]==nums[mid+1]) or  (mid%2==1 and nums[mid]==nums[mid-1]):
            left=mid+1

        else:
            right=mid-1
    return -1


res=singleNonDuplicate([1,1,2,3,3,4,4,5,5,6,6])
print(res)


