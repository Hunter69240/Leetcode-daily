def a():
    # INPUT:
    # prices[i] = price of stock on day i
    prices = [1, 2]

    # GREEDY SETUP:
    # profit → best profit found so far
    profit = 0

    # min_price → cheapest price seen before current day
    # acts as best buying point so far
    min_price = prices[0]

    # ITERATE:
    # treat each index as a potential SELL day
    for i in range(1, len(prices)):

        # --- INTERPRETATION (CORE THINKING) ---

        # Step 1: "Assume today is the selling day"
        # current selling price = prices[i]

        # Step 2: "Buy at the cheapest price seen before today"
        # best buy = min_price

        # Step 3: "Compute profit if we sell today"
        # candidate profit = prices[i] - min_price

        # Step 4: "Compare with best profit so far"
        # either:
        # - take this transaction
        # - or ignore and keep previous best
        profit = max(prices[i] - min_price, profit)

        # Step 5: "Update best buying opportunity"
        # include current price for future decisions
        min_price = min(prices[i], min_price)

        # Why this order:
        # First we try to SELL today using the best BUY price from earlier days.
        # Then we update the best BUY price to include today for future days.
        #
        # If we update min_price first, it might become today's price.
        # Then profit becomes (today - today) = 0,
        # which means buying and selling on the same day — not allowed.
        #
        # So:
        # 1. Use past data → calculate profit
        # 2. Then include today → update min_price

        
        # AFTER ITERATION:
        # min_price = minimum price in [0 … i]
        # profit = best achievable profit in [0 … i]

    return profit


print(a())


'''
prices = [1, 2]

Initial:
min_price = 1
profit = 0

i = 1:

    Assume sell today → price = 2

    Buy at cheapest before → 1

    candidate profit = 2 - 1 = 1

    compare with existing → max(1, 0) = 1

    update min_price → min(2, 1) = 1

Final:
profit = 1
'''