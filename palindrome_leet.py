def isPalindrome(x):
        
        #turning our integer into a string
        #then we turn it into a list to break it up into single digits
        numString = str(x)
        numList = list(numString)
        #now we use a for loop to reverse the number string and add each digit one by         #one into a new array
        numList2 = []
        for i in range(len(numList)-1, -1, -1):
            numList2.append(numList[i])
        
        #now we check if our two lists are equivalent
        if numList == numList2:
            return True