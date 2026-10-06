from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)

        for num in nums: # O(n)
            d[num] += 1

        k_most_frequent_nums = []

        # Find the most frequent num and delete it from dict
        # repeat this k times - k . O(n)
        for i in range(k): 
            # Find the most frequent num in each iteration
            most_frequent_num = nums[0]
            frequency = 0

            for k, v in d.items(): # O(n)
                if v > frequency:
                    most_frequent_num = k
                    frequency = v

            k_most_frequent_nums.append(most_frequent_num)
            # Delete the num to find the next most frequent ones
            del d[most_frequent_num]

        return k_most_frequent_nums







        