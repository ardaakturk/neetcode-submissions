class Solution:
    """
    If we find to zeros in nums, then result will be automatically all zeros.

    If we find one zero in given nums list,
    all numbers in result will be zeros
    except the number that has the same index with zero in the given nums list
    """
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_count = 0
        product = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        res = [0] * len(nums)

        if zero_count > 1:
            return res

        if zero_count == 1:
            # Find the index of the zero
            z_index = nums.index(0)
            res[z_index] = product
            return res

        for i in range(len(nums)):
            res[i] = product // nums[i]

        return res