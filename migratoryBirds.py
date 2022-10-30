#hackerrank migratoryBirds problem

###given an array arr that contains integers representing the id of various
#migratory birds, return the id that occurs most frequently
#if 2 id's have the max frequency, return the one with the lower id value

def migratoryBirds(arr):
    #create a dictionary of bird ids and their counts
    bd = dict()
    #iterate over arr to create dict
    for i in arr:
        if i in bd:
            bd[i] += 1
        else:
            bd[i] = 1
    #iterate over our dict to find the key with the highest value
    mostFrequent = []
    mF = 0
    for key in bd:
        if bd[key] > mF:
            mF = bd[key]
    #now that we have the most frequent value, we can go back and find any key with that value
    #then append the key to our mostFrequent array
    for key in bd:
        if bd[key] == mF:
            mostFrequent.append(key)
    #now we check if there is only a single key in mostFrequent and return its key
    if len(mostFrequent) == 1:
        return mostFrequent[0]
    #otherwise return key with lowest val
    return min(mostFrequent)

