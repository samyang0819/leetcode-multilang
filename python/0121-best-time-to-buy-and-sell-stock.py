class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

# Example usage:
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))  # Output: 0