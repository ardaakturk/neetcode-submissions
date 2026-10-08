class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        res = [0] * n

        res[0] = 1
        res[n - 1] = 1

        # Forward pass on result array
        prefix = 1
        for i in range(1, n):
            res[i] = prefix * nums[i - 1]
            prefix *= nums[i - 1]

        # Backward pass on result array
        postfix = 1
        for i in range(n - 2, -1, -1):
            res[i] *= nums[i + 1] * postfix
            postfix *= nums[i + 1]

        return res