class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #using a dictionary to track the number of occurences of each value
        numCounts = dict()
        for i in nums:
            numCounts[i] = numCounts.get(i, 0) + 1
            
        #now we return the number that only occurs once
        for val, count in numCounts.items():
            if count == 1:
                return val