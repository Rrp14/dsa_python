"""positive array only it works"""
def find_subarray(arr, k):
    n = len(arr)
    max_index = 0
    count = 0
    left = 0
    right = -1
    total_sum = 0

    for i in range(0, n):

        for j in range(i, n):
            total_sum += arr[j]
            right += 1

            if total_sum == k:
                count = right - left + 1


            elif total_sum > k:
                left += 1
                right = left - 1
                break

        if count > max_index:
            max_index = count
        count = 0
        total_sum = 0

    return max_index


ans=find_subarray([1, -1, 5, -2, 3], 3)

print(ans)


"""better code"""


class Solution:
    # Function to find the length of longest subarray having sum k
    def longestSubarray(self, nums, k):
        n = len(nums)

        # To store the maximum length of the subarray
        maxLen = 0

        # Pointers to mark the start and end of window
        left = 0
        right = 0

        # To store the sum of elements in the window
        sum = nums[0]

        # Traverse all the elements
        while right < n:

            # If the sum exceeds K, shrink the window
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1

            # Store the maximum length
            if sum == k:
                maxLen = max(maxLen, right - left + 1)

            right += 1
            if right < n:
                sum += nums[right]

        return maxLen


nums = [10, 5, 2, 7, 1, 9]
k = 15

# Creating an object of Solution class
sol = Solution()

# Function call to find the length
# of longest subarray having sum k
ans = sol.longestSubarray(nums, k)

print(f"The length of longest subarray having sum k is: {ans}")
