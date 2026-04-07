from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        return self.binary_search(nums, low, high, target)

    def binary_search(self, nums: List[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
            return self.binary_search(nums, low, high, target)
        else:
            high = mid - 1
            return self.binary_search(nums, low, high, target)






