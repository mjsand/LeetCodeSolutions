class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #first we trim any leading or trailing whitespace from s
        s = s.strip()
        #then we turn it into an array of words so we can iterate over it
        s_split = s.split()
        #now we find the length of s_split so we can grab the last word
        s_len = len(s_split)
        #now we can return the length of the last word
        return len(s_split[s_len - 1])
        
        
        
        