class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,best = 0,0
        #[10,1,5,6,7,1]
        for r in range(len(prices)):
            if(prices[l] > prices[r]):
                l=r
            best = max(best, prices[r]-prices[l])
        return best