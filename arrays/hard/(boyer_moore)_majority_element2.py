from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        cd1 = None
        cd2 = None
        count1 = 0
        count2 = 0

        for num in nums:
            if num == cd1:
                count1 += 1
            elif num == cd2:
                count2 += 1
            elif count1 == 0:
                cd1 = num
                count1 = 1
            elif count2 == 0:
                cd2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for num in nums:
            if cd1 == num:
                count1 += 1
            elif cd2 == num:
                count2 += 1

        res = []

        if count1 > (n / 3):
            res.append(cd1)
        if count2 > (n / 3):
            res.append(cd2)
        return res





