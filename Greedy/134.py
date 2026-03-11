class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 🚗 PROBLEM TYPE:
        # "Gas Station" — We need to find a station index from which we can start driving
        # clockwise around all gas stations and return back to the same starting point.
        #
        # gas[i]  = amount of fuel available at station i (fuel we GAIN)
        # cost[i] = fuel required to travel from station i to station (i + 1) clockwise (fuel we SPEND)
        #
        # At each station:
        #   1. Fill gas[i]
        #   2. Spend cost[i] to go to next station
        #   → Net fuel change = gas[i] - cost[i]
        #
        # Our goal: find a starting station such that our fuel NEVER becomes negative
        # while traveling the full circle.

        # 🔍 Quick Feasibility Check — VERY IMPORTANT:
        # sum(gas) = total fuel available from all stations
        # sum(cost) = total fuel required to complete the entire loop
        #
        # If sum(gas) < sum(cost), then even if we start from the "best" station,
        # there is not enough total fuel available to finish the loop.
        # Therefore, trip is impossible → return -1 immediately.
        if sum(gas) < sum(cost):
            return -1

        total = 0  # Tracks tank balance while checking a candidate start
        res = 0    # Current candidate station to start from

        # 🧠 GREEDY INTUITION:
        # We try to identify the correct station to start from — NOT to simulate the whole circular trip.
        #
        # Why a greedy decision works:
        # As we iterate, if starting from 'res' causes our fuel to drop below zero at station 'i',
        # then res CANNOT be a valid starting point.
        #
        # Even more importantly:
        # ➤ None of the stations between res and i can be a valid start either,
        #    because they would have even LESS fuel before reaching where we failed.
        #
        # Therefore, if we fail at 'i', the ONLY possible next candidate is 'i + 1'.
        # We skip the entire failed region in one step (this makes the algorithm O(n)).

        for i in range(len(gas)):
            total += gas[i] - cost[i]  # Net fuel change at station i

            # 🔥 If fuel goes negative → this start attempt failed
            if total < 0:
                total = 0          # Reset fuel for next start attempt
                res = i + 1        # Next station becomes new potential start

        # ❗ WHY WE DO NOT NEED TO SIMULATE THE CIRCULAR LOOP:
        # At this point, 'res' is the ONLY station that was never disproven.
        #
        # And because we already checked sum(gas) >= sum(cost),
        # we know the total amount of fuel in the full circle is enough,
        # so once we start from the correct 'res', the wrap-around (last station → first station)
        # will automatically succeed — we do NOT need to simulate the circular part again.
        #
        # So 'res' is guaranteed to be the answer.
        return res


"""
----------------------- 🔎 DETAILED DRY RUN -----------------------

Example:
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

Net gas at each station = gas[i] - cost[i] = [-2, -2, -2, +3, +3]

Start = 0, total = 0
i = 0 → total = -2 → FAIL → reset total = 0 → start = 1
i = 1 → total = -2 → FAIL → reset total = 0 → start = 2
i = 2 → total = -2 → FAIL → reset total = 0 → start = 3
i = 3 → total = +3 → OK
i = 4 → total = +3 + 3 = +6 → OK

Loop ends → result = 3

Explanation:
Starting from station 3, fuel never becomes negative while going forward.
Since total gas ≥ total cost, the remaining wrap (after station 4 → 0 → 1 → 2 → 3)
also succeeds — so 3 is the correct answer.

----------------------- ⚙️ WHY GREEDY SOLUTION IS CORRECT -----------------------

✓ A failure at station j means every station between the current start and j
  is impossible as a start (they would fail earlier or at the same place).

✓ Skipping all invalid start candidates makes the algorithm O(n) — no backtracking.

✓ Since sum(gas) ≥ sum(cost), we KNOW there exists a valid start,
  and the greedy scan leaves us with the only station that never failed → guaranteed answer.

Time Complexity:  O(n)   (single pass)
Space Complexity: O(1)   (constant memory)

"""
