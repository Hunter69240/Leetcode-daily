# Problem Type:
# Greedy / Simulation
# Goal: For each customer, give correct change using available bills
# lemonade costs = $5
# bills can be = [5,10,20]
# we start with no money

# Strategy:
# maintain count of $5 and $10 bills
# always prefer giving 10+5 for 20 (saves more $5 bills)

class Solution:
    def lemonadeChange(self, bills):
        
        # count of $5 bills
        five = 0
        
        # count of $10 bills
        ten = 0
        
        # process customers in order (queue)
        for bill in bills:
            
            # case 1: customer gives $5
            # no change needed
            # just collect the bill
            if bill == 5:
                five += 1
            
            # case 2: customer gives $10
            # must return $5
            elif bill == 10:
                
                # if no $5 available -> cannot give change
                if five == 0:
                    return False
                
                # give one $5
                five -= 1
                
                # collect $10
                ten += 1
            
            # case 3: customer gives $20
            # must return $15
            else:
                
                # prefer giving 10 + 5
                # because it preserves more $5 bills
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                
                # otherwise give three $5 bills
                elif five >= 3:
                    five -= 3
                
                # cannot give change
                else:
                    return False
        
        # all customers served successfully
        return True



# -------------------------
# DRY RUN
# bills = [5,5,5,10,20]
# -------------------------

# start
# five=0 ten=0

# bill = 5
# five=1 ten=0

# bill = 5
# five=2 ten=0

# bill = 5
# five=3 ten=0

# bill = 10
# give one 5
# five=2 ten=1

# bill = 20
# give 10+5
# five=1 ten=0

# end -> return True



# -------------------------
# Example Fail Case
# bills = [5,5,10,10,20]
# -------------------------

# five=0 ten=0

# 5 -> five=1
# 5 -> five=2
# 10 -> give 5 -> five=1 ten=1
# 10 -> give 5 -> five=0 ten=2
# 20 -> need 15

# try 10+5
# no five available

# try 5+5+5
# not enough

# return False



# Time Complexity:
# O(n)

# Space Complexity:
# O(1)