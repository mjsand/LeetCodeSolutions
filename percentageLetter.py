class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        #initialize a count to 0, iterate over s and increment count every time i matches letter
        count = 0
        for i in s:
            if i == letter:
                count += 1
                
        #now we have a count of occurences of letter in s, we can now calculate the % occurence using
        #the length of s
        
        return trunc((count/(len(s))) * 100)