class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1


