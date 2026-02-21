from collections import Counter
from typing import List


def singleNumber( nums: List[int]) -> int:
    freq = Counter(nums)
    key = 0
    for k, v in freq.items():
        if v == 1:
            key = k
    return key