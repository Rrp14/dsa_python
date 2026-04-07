from typing import List


def findRotations(nums: List[int]) -> int:
    n = len(nums)
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:

            left = mid + 1
        else:
            right = mid
    return left


res = findRotations([4,5,6,7,0,1,2,3])
print(res)




