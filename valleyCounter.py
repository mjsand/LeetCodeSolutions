def countingValleys(steps, path):
    altitude = 0
    valleyCounter = 0
    
    #now we can iterate over the path as individual characters
    for step in range(steps):
        print(path[step])
        if path[step] == 'U':
            altitude += 1
        else:
            altitude -= 1
        #now we check if altitude is zero, and the last step was up
        #this would indicate we just left a valley
        print(altitude)
        if altitude == 0 and path[step] == 'U':
            print('in valleyCounter')
            valleyCounter += 1
        print(valleyCounter)
    return valleyCounter

path1 = 'UUDD'
path2 = 'UDU'
path3 = 'DUDU'

#vc1 = countingValleys(len(path1), path1)
#print("Valley Counter: ", vc1)

#vc2 = countingValleys(len(path2), path2)
#print(vc2)

vc3 = countingValleys(len(path3), path3)
print('Valley Counter: ', vc3)