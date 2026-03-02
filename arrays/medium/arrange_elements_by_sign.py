"""brute_force"""
from typing import List


def rearrangeArray(nums: List[int]) -> List[int]:
    temp_pos = []
    temp_neg = []

    for num in nums:
        if num > 0:
            temp_pos.append(num)
        else:
            temp_neg.append(num)

    nums[0] = temp_pos[0]
    nums[1] = temp_neg[0]

    od = 1
    ev = 1

    for i in range(2, len(nums)):
        if i % 2 == 0:
            nums[i] = temp_pos[ev]
            ev += 1
        else:
            nums[i] = temp_neg[od]
            od += 1

    return nums

"""optimal"""


def rearrangeArray_op(nums: List[int]) -> List[int]:
    n = len(nums)
    temp = [0] * n
    i = 0
    j = 1

    for num in nums:
        if num > 0:
            temp[i] = num
            i += 2
        else:
            temp[j] = num
            j += 2
    return temp


