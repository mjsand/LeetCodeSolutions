##given two arrays of integers, A and B, and an integer k, determine if any combination
##of the two arrays in any order of their values will produce A[i] + B[i] >= k

def twoArrays(k, A, B):
    #sort A in ascending order
    A.sort()
    #sort B in descending order
    B.sort(reverse=True)
    #now we iterate and check the worst-case scenario where every A[i] + B[i] >= k
    #since we have matched up A's smallest value with B's greatest value
    
    for i in range(len(A)):
        #if we find any instance of it not holding up, return NO
        if A[i] + B[i] < k:
            return 'NO'
    #if we complete the loop with returning NO, return YES
    return "YES"