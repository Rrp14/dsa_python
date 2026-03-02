from typing import List


def longestConsecutive(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 1
    nums = list(set(nums))
    nums.sort()
    max_seq = 0
    prev = nums[0]
    cur = 1

    for num in nums[1:]:
        if num == prev + 1:
            cur += 1

        else:
            max_seq = max(cur, max_seq)
            cur = 1
        prev = num
    return max(cur, max_seq)
