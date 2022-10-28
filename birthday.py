###this function, given an array of ints s, a value d and value m, will return the number
#of subarrays of length m, in which the elements of each subarray can sum up to equal d


def birthday(s, d, m):
    #create array to add our solutions into
    solutions = []
    #we need to find all the subarrays inside s that are of length m, starting at the first value
    #we iterate from 0, to len(s)-m+1 which will prevent us from going out of bounds will still getting
    #every possible subarray of length m
    for i in range(0, len(s)-m+1):
        #a will be our created subarray
        a = []
        #now we take each element from i, to i+m and append it into a
        for j in range(i, i+m):
            a.append(s[j])
        #asum will be the sum of all the elements in each subarray, a
        aSum = 0
        #now we iterate over a to find the sum of its elements
        for k in a:
            aSum += k
        #we check to see if the sum of the elements of a equal d
        if aSum == d:
            #if so, append a into solutions
            #solutions we be an array of arrays of the possible solutions
            solutions.append(a)
    #return the length of solutions as this will be the number of possible solutions
    return len(solutions)
        