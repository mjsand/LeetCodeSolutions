class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        #if it is in our array, return the index
        if target in nums:
            return nums.index(target)
        
        #checking first if target is the smallest or the largest in the array
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return (len(nums))
        
        #otherwise we will need to iterate over the list to find where it should go
        lower = 0
        lower_index = 0
        for i in nums:
            if i < target:
                lower = i
                lower_index = nums.index(lower)
                
        return (lower_index+1)
        
            