from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_seen = {}
        prefix_sum = 0
        count = 0
        prefix_sum_seen[0] = 1

        for i in range(len(nums)):
            prefix_sum += nums[i]

            rem = prefix_sum - k

            if rem in prefix_sum_seen:
                count += prefix_sum_seen[rem]

            prefix_sum_seen[prefix_sum] = prefix_sum_seen.get(prefix_sum, 0) + 1

        return count

