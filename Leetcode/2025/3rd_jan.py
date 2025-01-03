class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        # Calculate the prefix sum array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        total_sum = prefix[-1]
        valid_splits = 0

        # Iterate through the array to find valid splits
        for i in range(n - 1):
            left_sum = prefix[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                valid_splits += 1

        return valid_splits