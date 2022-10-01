class Solution:
    def reverse(self, x: int) -> int:
        
        #first we convert the integer to a string
        s = str(x)
        #then to a list
        l = list(s)
        #now we can reverse the string, concatenate it, and convert back to an integer
        l.reverse()
        a = l[0]
        #now we check to see if x was originally a negative number
        if "-" in l:
            l.remove("-")
            l[0] = "-" + a
            
        s2 = ""
        for i in l:
            s2 = s2 + i
            
        out = int(s2)
        #now we have to check for instances where reversing x would exceed the 32 bit output constraint
        if out > 2**31 - 1:
            return 0
        elif out < -2**31:
            return 0
        else:
            return out
