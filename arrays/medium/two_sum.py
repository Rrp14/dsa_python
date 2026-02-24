"""using bruteforce"""
from typing import List


def two_sum_hm(arr,target):
    n=len(arr)

    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return i,j


    return None


arr=[2,6,5,8,11]
print(two_sum_hm(arr,14))


"""using hashmap"""

def twoSum( nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):

            comp = target - num

            if comp in seen:
                return [seen[comp], i]

            seen[num] = i
        return []

