# Calculates the maximum profit from buying and selling stock on different days
# Uses one-pass greedy approach: track the minimum price so far and compute profit on each day
# Keeps updating the maximum profit whenever a better sell opportunity is found

prices = [7, 1, 5, 3, 6, 4]

min_price = float('inf')  # Initialize with a very large number
max_profit = 0            # Maximum profit seen so far

# Iterate through all prices
for price in prices:
    if price < min_price:
        min_price = price  # Found a new lower price to buy at
    else:
        profit = price - min_price  # Calculate profit if sold at current price
        if profit > max_profit:
            max_profit = profit     # Update max profit if current profit is better

print(max_profit)  # Final result: maximum profit possible
