class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cheapest_index, cheapest_price = 0, prices[0]
        max_pf = 0

        for i in range(len(prices)):
            if prices[i] < cheapest_price:
                cheapest_price = prices[i]
                cheapest_index = i
            max_pf = max(max_pf, prices[i] - cheapest_price)
        
        return max_pf









        