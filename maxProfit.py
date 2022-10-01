class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = sorted(prices,reverse=True)
        #first we check the worst-case scenario where the prices are all in
        #descending order which means no profit is possible
        if(p==prices):
            return 0
        #now we return result if prices only has 2 values in it
        if len(prices)==2:
            return prices[1]-prices[0]
        
        #otherwise we will need to solve with the following algorithm
        #we set sell equal to the second value in prices, and buy to the first value
        else:
            sell = prices[1]
            buy=prices[0]
            l = []
            #now we iterate over prices starting at index 1
            for i in range(1,len(prices)):
                #if the previous prices value is greater than or equal to buy and                     #i-1<i
                #we set buy equal to the previous value in prices
                if prices[i-1]<=buy and i-1<i:
                    buy=prices[i-1]
                #if the current prices value is greater than or equal to buy and
                #i>i-1
                #we set sell equal to the current prices value, and add the 
                #difference between sell and buy to our list
                if prices[i]>=buy and i>i-1:
                    sell = prices[i]
                    l.append(sell-buy)
            #now we return the highest profit value from our list  
            return max(l)
                