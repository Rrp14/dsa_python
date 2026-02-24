from typing import List

"""two pass"""
def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    w = 0
    r = 0
    b = 0
    for i in range(0, n):
        if nums[i] == 0:
            r += 1
        elif nums[i] == 1:
            w += 1
        else:
            b += 1

    nums[:] = [0] * r + [1] * w + [2] * b

"""brute force"""

def sortColors_bf(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]



"""dutch national flag /one pass"""

def sort_colors_dnf(nums:List[int])->None:

    n=len(nums)

    mid=low=0
    high=n-1

    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1

        elif nums[mid]==1:
            mid+=1

        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1




