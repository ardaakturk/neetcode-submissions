from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen_nums = set(nums)
        starters = defaultdict(int)

        for num in seen_nums:
            if (num - 1) in seen_nums:
                # This number cannot be a starter of a consecutive sequence
                continue 
            conseq_length = 1
            next_num = num + 1
            while next_num in seen_nums:
                conseq_length += 1
                next_num += 1

            starters[num] = conseq_length

        max_conseq_length = starters[0]
        for k, v in starters.items():
            if v > max_conseq_length:
                max_conseq_length = v

        return max_conseq_length