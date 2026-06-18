class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_of_numbers = dict()


        """
        iterate through the list:
         - remainder = target - current_num
         - if remainder is available in the hashmap, 
           then return the indices of current_num and remainder.
         - if not, then add the current_num and its index to the hashmap
        """
        for i in range(len(nums)): # O(n)
            remainder = target - nums[i]
            if remainder in indices_of_numbers: # O(1)
                return [indices_of_numbers[remainder], i]
            else:
                # Add the number to the hashmap only if not exists,
                # Otherwise we would keep the greater index
                if nums[i] not in indices_of_numbers:
                    indices_of_numbers[nums[i]] = i # O(1)



                




        