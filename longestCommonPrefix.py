class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #first check for empty list
        if len(strs) == 0:
            return ""
        #get the shortest word in strs since all the longer word would have to
        #contain at least part of the shortest word
        pref = min(strs)
        
        #iterate over strs
        for i in strs:
            #if a word does not start with our prefix, we remove a letter from our prefix one at a time
            while not i.startswith(pref):
                pref = pref[:-1]
        #return the remaining prefix   
        return pref
        
                