## this function takes a given array of integers and a target integer, and returns indices of the two numbers in the array
## that add up to the target integer value

nums = [2, 4, 3, 1, 7, 8]
target = 15

def TwoSum(nums, target):
    ##instantiating a dictionary to store our indices in
        values = {}
        ##enumerating nums to create an enumerated list containing the index and value of each item in nums
        ##this allows us to iterate over nums a single time while checking for a pair that adds up to target
        ##if one is found, then it will be returned as a list pair
        for indx, val in enumerate(nums):
            if target - val in values:
                return [values[target-val], indx]
            ##if it is not found in the previous iteration, then the previous index of val is stored in values
            else:
                values[val] = indx
        
TwoSum(nums, target)
                
