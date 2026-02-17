from typing import List
"""given and array and integer k right shift elements by k 
easy is using temp array"""

def rotate(nums: List[int], k: int) -> None:

    n = len(nums)
    temp = [0] * n
    for i in range(n):
        temp[(i -k) % n] = nums[i]

    for i in range(n):
        nums[i] = temp[i]




nums =[1, 2, 3, 4, 5]
rotate(nums, 1)
print(nums)


def rotate_rev_left(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n

    rev(nums, 0, k - 1)
    rev(nums, k, n - 1)
    rev(nums, 0, n - 1)



def rev(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


nums = [1, 2, 3, 4, 5]
rotate_rev_left(nums, 1)
print(nums)

