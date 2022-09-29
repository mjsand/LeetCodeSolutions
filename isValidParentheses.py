class Solution:
    def isValid(self, s: str) -> bool:
        #first make sure the length of s is even
        if len(s) % 2 == 1:
            return False
        
        #create lists of opening and closing brackets
        open = [ "(", "[", "{" ]
        close = [ ")", "]", "}" ]
        #create a dictionary of bracketing pairs
        pairs = dict(( "()", "[]", "{}" ))
        #create a stack to add openers to
        stack = []
        
        #now we iterate over s to see if it is a valid string
        for i in s:
            if i in open:
                stack.append(i)
            elif len(stack) == 0 or i != pairs[stack.pop()]:
                return False
            
        #check length of stack is 0 at end
        return len(stack) == 0
        