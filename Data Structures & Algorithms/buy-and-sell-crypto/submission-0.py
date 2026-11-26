class Solution:
    
    # Define a method that takes a list of stock prices and returns the maximum profit as an integer
    def maxProfit(self, prices: List[int]) -> int:

        # Assume the first day's price is the lowest buying price so far
        buy_value = prices[0]

        # Keep track of the maximum profit found so far
        curr_profit = 0


# Keep track of the maximum profit found so far
        for i in range(1, len(prices)):

            # Check if today's price is higher than our buying price
            if buy_value < prices[i]:

                # Calculate the profit if we sell at today's price
                new_profit = prices[i] - buy_value

                # Update the maximum profit if today's profit is higher
                if new_profit > curr_profit:
                    curr_profit = new_profit


            # If today's price is lower than our current buying price,
            # update the buying price to today's price
            # We also make sure today is not the last day
            if buy_value > prices[i] and i != len(prices) - 1:
                buy_value = prices[i]


        # Return the maximum profit found
        return curr_profit