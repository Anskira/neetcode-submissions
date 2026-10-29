class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # profit = 0

        # for i in range(len(prices)-1):

        #     for j in range(i+1, len(prices)):
        #         temp = prices[j]-prices[i]
        #         if temp>profit:
        #             profit = temp
        
        # return profit

        l, r = 0, 1
        max = 0
        while r<len(prices):

            if prices[l]<prices[r]:
                if prices[r]-prices[l]>max:
                    max = prices[r] - prices[l]

            else:
                l=r
            
            r+=1

        return max