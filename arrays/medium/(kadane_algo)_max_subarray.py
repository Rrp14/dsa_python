from typing import List

"""doesnt work for large numbers"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       n=len(nums)
       if n==1:
            return nums[0]

       total=0
       largest_sum=float("-inf")

       for i in range(0,n):
            total+=nums[i]
            for j in range(i+1,n):
                total+=nums[j]

                if total>largest_sum:
                    largest_sum=total
            total=0

       return largest_sum



"""kadane algorithm"""


def maxSubArray(nums: list[int]) -> int:
    maxi = float('-inf')
    sum = 0

    for i in range(len(nums)):

        sum += nums[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi



"""to print largest subarray"""

def maxSubArray_print(nums: list[int]) -> List[int]:
    maxi = float('-inf')
    sum = 0
    start=0
    ans_start=-1
    ans_end=-1

    for i in range(len(nums)):

        sum += nums[i]

        if sum > maxi:
            maxi = sum
            ans_start=start
            ans_end=i

        if sum < 0:
            sum = 0
            ans_start=0
            ans_end=0
            start=i+1


    return [maxi,ans_start,ans_end]


nums=[2, 3, 5, -2, 7, -4]
ans=maxSubArray_print(nums)

i=ans[1]
j=ans[2]

print(f"maximum sub array is {ans[0]}")
for k in range(i,j+1):
    print(nums[k],end=" ")