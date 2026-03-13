from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[intervals[0]]
        i=0
        for inter in intervals[1:]:
            if  inter[0]<=result[i][1]:
                result[i][1]=max(result[i][1],inter[1])

            else:
                result.append(inter)
                i+=1
        return result