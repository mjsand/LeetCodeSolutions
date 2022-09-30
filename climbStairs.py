class Solution:
    def climbStairs(self, n: int) -> int:
        
        #first we handle the edge cases
        if n == 0 or n == 1 or n == 2:
            return n
        
        #now we can use pointers to create a formula that will calculate the number
        #of ways to get to the top since it is the sum of the 2 previous values
        prevPrev = 1
        prev = 2
        curr = 0
        
        for i in range(3, n+1):
            curr = prev + prevPrev
            prevPrev = prev
            prev = curr
            
        return curr
            
            