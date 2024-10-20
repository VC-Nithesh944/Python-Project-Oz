#This solution has a Time complexity of O(N) and runtime of 50ms.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1     #skipping 0th index as it is compulsory and this pointer is for assigning
        seen = 1  #because the first element is seen
        for j in range(1,len(nums)):   #j should run from 1 to last index
            if nums[j-1] == nums[j]:
                seen += 1
            else:
                seen = 1
              
            if seen <= 2:            #should copy the elements if seen less than 2 or 2 times
                nums[i] = nums[j] 
                i += 1
        return i
