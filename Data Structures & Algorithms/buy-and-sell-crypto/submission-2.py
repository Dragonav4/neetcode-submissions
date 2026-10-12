class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,best = 0,0
        #[10,1,5,6,7,1]
        for r in range(len(prices)): #l=0, r=1, ### l=1,r=2
            if(prices[l] > prices[r]): # 10 > 1 -> l=1 ## 1 > 5 ?
                l=r
            best = max(best, prices[r]-prices[l]) # best = 0 ## best = 5-1=4
        return best