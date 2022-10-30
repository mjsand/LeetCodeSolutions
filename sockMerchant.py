##this program, given an input array ar and its length, n, contains integers
#this program will return the number of pairs of integers in ar
#by first creating a dictionary with the integers as keys, then finding the total number
#of pairs

def sockMerchant(n, ar):
    #create a dictionary that holds the sock value as key, and its count as its value
    sd = dict()
    #iterate over the input array and create the dictionary
    for i in ar:
        if i not in sd:
            sd[i] = 1
        else:
            sd[i] += 1
    #now we have our dictionary with values
    pairs = 0
    #now we can iterate over the keys in our dict, get the value at each key
    #perform floor division by 2 to get the number of pairs, and increment
    #pairs by that value
    for key in sd:
        val = sd.get(key)
        floorVal = val // 2
        pairs += floorVal
        
    return pairs
    