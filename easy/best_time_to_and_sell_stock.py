from typing import List


class Solution:
    # sol1: Brute Force
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices[:-1]):
            profit = max(prices[i+1:]) - price
            if max_profit < profit:
                max_profit = profit
        return max_profit

    # sol2: one pass
    def maxProfit2(self, prices: List[int]) -> int:
        max_profit = 0
        if prices:
            min_price = prices[0]
            for price in prices[1:]:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                elif price < min_price:
                    min_price = price
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit2([7,1,5,3,6,4]))
    print(sol.maxProfit2([7,6,4,3,1]))


