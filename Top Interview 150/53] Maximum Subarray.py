#This has a runtime of 23ms but time complexity of O(N) and Space complexity of O(1).
# I have used kadane's algorithm solve this program

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = -10000
        for i in nums:
            sum += i
          
            if max<sum:
                max=sum
              
            if sum<0:
                sum=0
              
        return max
