from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            ans = mid

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if nums[ans] >= target:
            return ans
        else:
            return ans + 1




