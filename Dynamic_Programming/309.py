class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State machine: Two states - "buying" (can buy stock) or "selling" (can sell stock)
        # If buying -> move to i+1 (next day)
        # If selling -> move to i+2 (skip one day for cooldown)

        # Memoization dictionary: key=(index, buying_state), value=max_profit from this state
        dp = {}  

        def dfs(i, buying):
            # Base case: If index exceeds array length, no more transactions possible
            if i >= len(prices):
                return 0
            
            # Return cached result if this state was already computed
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # State: Currently in "buying" mode (can purchase stock)
            if buying:
                # Option 1: Buy stock at current price
                # Move to next day (i+1) in "selling" mode, subtract current price (cost)
                buy = dfs(i+1, not buying) - prices[i]
                
                # Option 2: Skip this day (cooldown), stay in "buying" mode
                cooldown = dfs(i+1, buying)
                
                # Take the maximum profit from both options
                dp[(i, buying)] = max(buy, cooldown)
            
            # State: Currently in "selling" mode (holding stock, can sell)
            else:
                # Option 1: Sell stock at current price
                # Move to i+2 (skip next day for mandatory cooldown), add current price (profit)
                sell = dfs(i+2, not buying) + prices[i]
                
                # Option 2: Skip this day (cooldown), stay in "selling" mode (keep holding)
                cooldown = dfs(i+1, buying)
                
                # Take the maximum profit from both options
                dp[(i, buying)] = max(sell, cooldown)
            
            return dp[(i, buying)]
        
        # Start DFS from day 0 in "buying" state (initially can buy)
        return dfs(0, True)
