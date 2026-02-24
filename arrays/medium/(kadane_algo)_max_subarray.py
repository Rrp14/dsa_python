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