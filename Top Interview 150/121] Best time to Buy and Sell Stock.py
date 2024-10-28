# Has runtime of 23ms and Time complexity of O(N) beats 93%
# price is itself the element 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 10000
        profit = 0
        for price in prices:
            if price < min:
                min = price
            if price - min > profit:
                profit = price - min
        return profit
