import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        if len(nums) > threshold:
            return -1

        def helper(nums, div):
            t = 0
            for num in nums:
                t += math.ceil(num / div)
            return t

        left, right = 1, max(nums)
        ans = max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            if helper(nums, mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans




