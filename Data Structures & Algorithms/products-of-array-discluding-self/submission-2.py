class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        # Forward pass to fill the prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Backward pass to fill the suffix array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Compose the result array
        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res