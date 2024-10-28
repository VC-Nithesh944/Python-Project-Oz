#This has runtime of 0ms and Time complexity of O(N) beats 100%.
#This has simpler logic than the easy level question 121].
#Using parantheses Slows down the function.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
