#this code is for the hackerRank problem 'MarsExploration'

#a string s is provided of all uppercase letters, with len(s)%3 = 0
#s is a combination of 'SOS' repeated any number of times
#the objective is to determine how many of the letters were changed by radiation

#this function will analyze the provided string s and determine the number of letters that are
#either totally wrong or out of place

def marsExploration(s):
    #truncate the message for comparison
    #initialize variables for the number of incorrect characters where an 'O' or 'S' should be
    #sPos is the position we expect to find S in the string s
    #loopCount counts the number of iterations in our while loop that is used to increment
    #sPos at the expected intervals
    oCount = 0
    loopCount = 0
    sCount = 0
    sPos = 0
    #we expect to find an 'O' starting at position 1, and always incrementing by 3
    for i in range(1, len(s), 3):

        if s[i] != 'O':
            print(s[i])
            oCount += 1
    #we expect to find 'S' starting at position 0, then incrementing by 2, then 1, then 2, ... etc.
    while sPos < len(s):
        loopCount += 1
        if s[sPos] != 'S':
            print(s[sPos])
            sCount += 1
        
        if loopCount % 2 == 0:
            sPos += 1
        else:
            sPos += 2
    return oCount + sCount