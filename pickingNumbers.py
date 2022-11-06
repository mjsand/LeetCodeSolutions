###this function, given an array of integers, 

def pickingNumbers(a):
    a.sort()
    subArrSize = 0
    maxSubArrSize = 0
    
    for i in range(len(a)):
        for j in range(i, len(a)):
            #first check if the absolute value is > 1
            if abs(a[i] - a[j]) > 1:
                break
            #otherwise increment the size of subArrSize
            else:
                subArrSize += 1
        #after breaking out of inner for loop, if subArrSize > maxSubArrSize then set max equal to it
        if subArrSize > maxSubArrSize:
            maxSubArrSize = subArrSize
        #reset subArrSize to 0 so we can start over creating a new subarray
        subArrSize = 0
        
    return maxSubArrSize