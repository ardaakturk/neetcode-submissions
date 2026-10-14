class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_pf = 0

        for window_length in range(1, len(prices)):
            i = 0
            j = i + window_length
    
            while j < len(prices):
                max_pf = max(max_pf, prices[j] - prices[i])
                i += 1
                j += 1
        
        return max_pf









        