"""brute force"""
from typing import List

def mov_zeroes(nums:List[int])->None:
    n=len(nums)

    temp=[0]*n
    k=0

    for i in range(n):
        if nums[i]!=0:
            temp[k]=nums[i]
            k+=1

    for i in range(n):
        nums[i]=temp[i]

nums=[1,0,5,0,0,8,4,0,2,3,0]
mov_zeroes(nums)
print(nums)



"""optimised"""
def moveZeroes( nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = -1

    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break

    if j == -1:
        return

    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1