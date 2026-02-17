from typing import List

"""check how many drops happens , since drop is  a deviation from increasing to decreasing 
or Because in a sorted (non-decreasing) array, numbers should never go down."""
def check(nums: List[int]) -> bool:
        n = len(nums)
        drops = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1

        if drops <= 1:
            return True
        else:
            return False



nums=[2,1,3,4]
print(check(nums))
