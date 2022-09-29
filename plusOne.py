class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #first we will convert the individual integers to strings and concatenate
        #them
        num_str = ""
        for i in digits:
            num_str = num_str + str(i)
            
        #now we can convert the whole thing back to a single number and add one to it
        output = int(num_str) + 1
        #now we need to split our output back up into a list
        output_to_str = str(output)
        out_list = list(output_to_str)
        #now we need to convert the individual string back to ints
        final_list = []
        for i in out_list:
            final_list.append(int(i))
            
        return final_list
        
        
        