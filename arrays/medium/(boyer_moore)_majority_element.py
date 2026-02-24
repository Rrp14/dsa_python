from collections import Counter
from typing import List


def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        n = len(nums)

        for k, v in freq.items():
            if v > n / 2:
                return int(k)
        return 0

"""Boyer Moore majority vote algorithm"""
from typing import List
def majorityElement_bmm( nums: List[int]) -> int:
        elem = nums[0]
        count = 1

        for num in nums[1:]:
            if count == 0:
                elem = num
                count = 1
                continue
            if num == elem:
                count += 1
            else:
                count -= 1

        return elem

majorityElement([3,2,3])





