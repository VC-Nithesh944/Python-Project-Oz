##This has a runtime of 0ms and Time complexity of O(N).
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 1                      #because the first element is already unique
        for j in range(len(nums)):
            if (nums[i] != nums[j]):
                i+=1
                nums[i] = nums[j]
                k+=1
        return k
