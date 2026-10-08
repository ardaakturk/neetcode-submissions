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
                if zero_count == 2:
                    return [0] * len(nums)
            product *= num

        if zero_count == 1:
            res = [0] * len(nums)
            z_index = nums.index(0)
            z_index_product = 1
            for i in range(len(nums)):
                if i == z_index:
                    continue
                z_index_product *= nums[i]
            res[z_index] = z_index_product
            return res

        res = [product] * len(nums)
        for i in range(len(nums)):
            res[i] = int(res[i] / nums[i])

        return res