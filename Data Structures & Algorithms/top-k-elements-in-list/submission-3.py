class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = dict()

        for num in nums: # O(n)
            d[num] = 1 + d.get(num, 0)

        frequency_bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in d.items():
            frequency_bucket[freq].append(num)

        result_list = []
        for i in range(len(frequency_bucket)-1, 0, -1):
            while len(frequency_bucket[i]) != 0:
                result_list.append(frequency_bucket[i].pop())
                if len(result_list) == k:
                    return result_list


