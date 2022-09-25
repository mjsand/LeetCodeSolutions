## this function takes a given array of integers and a target integer, and returns indices of the two numbers in the array
## that add up to the target integer value

nums = [2, 4, 3, 1, 7, 8]
target = 15

def TwoSum(nums, target):
    
        values = {}
        
        for indx, val in enumerate(nums):
            if target - val in values:
                return [values[target-val], indx]
            else:
                values[val] = indx
        
TwoSum(nums, target)
                