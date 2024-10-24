#This is the first problem in python that has got 0ms runtime and it was easy
#It has a time complexity of O(N) and space complexity of O(N).

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()                       #remove the trailing spaces
        count = 0
        for i in range(len(string)-1,-1,-1):     #loop from end of the string till 0 because -1 is excluded
            if string[i] == ' ' or string[i] == '\t': #as soon you encouter whitespace or tab return count else increment count.
                return count
            count+=1
        return count

