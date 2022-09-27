class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #creating our left point
        left = 1
        #r will be our right pointer and it will traverse the array
        for r in range(1, len(nums)):
            #each iteration we are checking for unique values; each time we find a unique value in the array,
            #we move it to position of the left pointer in the array
            #then we increment our left pointer value by one to keep scooting it forward in position
            if nums[r] != nums[r-1]:
                nums[left] = nums[r]
                left += 1
        
        return left
        
            