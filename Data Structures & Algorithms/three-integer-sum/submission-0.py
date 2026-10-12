class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        l = 0
        n = len(nums)
        while l < n - 2:
            m = l + 1
            r = n - 1
            while m < r:
                if nums[m] + nums[r] < -nums[l]:
                    m += 1
                elif nums[m] + nums[r] > -nums[l]:
                    r -= 1
                else:
                    comb = [nums[l], nums[m], nums[r]]
                    if comb not in res:
                        res.append(comb)
                    m += 1
            l += 1

        return res