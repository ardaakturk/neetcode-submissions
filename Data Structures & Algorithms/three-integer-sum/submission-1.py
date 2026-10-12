class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res = set()

        i = 0
        n = len(nums)

        while i < n - 2:

            a = nums[i]
            l, r = i + 1, n - 1

            if a > 0:
                # All remaining numbers are positive, cannot sum to zero
                break

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    comb = (a, nums[l], nums[r])
                    res.add(comb)
                    l += 1
            i += 1

        return [list(comb) for comb in res]