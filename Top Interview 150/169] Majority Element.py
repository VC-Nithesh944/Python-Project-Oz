#This program has a time complexity of O(N) and Space Complexity of O(N) and runtime of 7ms.
#this utilises Boyer - Moyers Voting Algorithm.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
        
