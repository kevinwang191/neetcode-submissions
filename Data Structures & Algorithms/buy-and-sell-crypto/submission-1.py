class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1 
        max_p = 0

        while j < len(prices):
            if prices[j] < prices[i]:
                i = j 
            else:
                profit = prices[j] - prices[i]
                max_p = max(max_p, profit)
            
            j+=1
        return max_p

        