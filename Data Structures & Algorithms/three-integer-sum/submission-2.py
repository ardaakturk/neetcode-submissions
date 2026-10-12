class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):

            # All remaining numbers are positive, cannot sum to zero
            if nums[i] > 0:
                break

            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return res