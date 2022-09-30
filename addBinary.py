class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #check the case both a and b are empty strings
        if a == "" and b == "" or a == "0" and b == "0":
            return "0"
        #turning both strings into lists so we can iterate over them
        aList = list(a)
        bList = list(b)
        #creating variables for our loop
        aPower = len(aList) - 1
        bPower = len(bList) - 1
        aVal = 0
        bVal = 0
        #now we iterate to sum up the values of a and b and turn them into integers
        for i in range(len(aList)):
            aVal += int(aList[i]) * (2**aPower)
            aPower -= 1
        
        for i in range(len(bList)):
            bVal += int(bList[i]) * (2**bPower)
            bPower -= 1
        
        #now we have converted both binary strings into their integer values
        #we can add them, then convert the result back to binary
        abSum = aVal + bVal
        #we set n equal to a very large number
        n = 100 
        output = ""
        #now we have a looped algorithm that will convert our numerical value
        #back to a binary string
        while n >= 0:
            if abSum / (2**n) < 1:
                output = output + "0"
                n -= 1
            else:
                output = output + "1"
                abSum -= (2**n)
                n -= 1
                
        #now we need to remove any leading zeros from our output string
        output = output.lstrip('0')
        #return the resulting string        
        return output
                