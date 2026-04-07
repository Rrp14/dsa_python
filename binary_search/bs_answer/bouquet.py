from typing import List


class Solution:
    def is_possible(self, bloomDay: List[int], D: int, m: int, k: int) -> int:
        bouquet = 0
        tally = 0

        for bloom in bloomDay:
            if bloom <= D:
                tally += 1
            else:
                bouquet += tally // k
                tally = 0
            if bouquet >= m:
                return True

        bouquet += tally // k

        return bouquet >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if (m * k) > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if self.is_possible(bloomDay, mid, m, k):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


