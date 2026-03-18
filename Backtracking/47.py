def permuteUnique(nums):
    nums.sort()           # ← CRITICAL: sort so duplicates are adjacent
    results = []
    
    def backtrack(current, remaining):
        # Base case: used all numbers
        if not remaining:
            results.append(current[:])
            return
        
        seen = set()      # track what values we've tried at THIS level
        
        for i in range(len(remaining)):
            if remaining[i] in seen:   # ← skip duplicate values
                continue
            
            seen.add(remaining[i])
            
            # Make choice
            current.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Recurse
            backtrack(current, new_remaining)
            
            # Undo choice ← this is the backtracking step
            current.pop()
    
    backtrack([], nums)
    return results