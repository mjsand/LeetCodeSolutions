class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        #we are going to enter a while loop to increment and find the closest integer 
        #to the square root without going over
        while True:
            num_squ = num * num
            if num_squ == x:
                return num
            elif num_squ  < x:
                num += 1
            elif num_squ > x:
                return num-1