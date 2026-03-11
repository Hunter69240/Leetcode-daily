class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 🃏 PROBLEM TYPE:
        # "Hand of Straights" — We must determine if the list `hand` can be rearranged
        # into groups of `groupSize` cards, where each group contains **consecutive**
        # integers (like forming straights in Rummy).
        #
        # Example: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
        # Valid straight grouping: [1,2,3], [2,3,4], [6,7,8]
        #
        # If we cannot partition `hand` into straight groups of size `groupSize`,
        # return False.

        # ✔ Quick Check:
        # To divide into groups of size k, total number of cards must be divisible by k.
        if len(hand) % groupSize != 0:
            return False

        # 🧮 Count frequency of each card
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # ⛰ Prepare a min-heap of unique card values so we can always pick the
        # smallest available card to start a new straight.
        minH = list(count.keys())
        heapq.heapify(minH)

        # 🧠 GREEDY INTUITION:
        # Always start forming the next straight beginning from the **smallest**
        # available card value.
        #
        # Why? If the smallest card cannot form a straight (example: missing next number),
        # then NO solution exists — because this smallest card cannot be skipped,
        # it MUST belong to some group and MUST start a straight.
        #
        # So repeatedly:
        #   - Take the smallest card → mark it as the first card in a new straight
        #   - Check if next (groupSize - 1) consecutive cards exist
        #   - Reduce counts and remove cards from heap when count reaches zero

        while minH:
            first = minH[0]  # smallest available card

            # Attempt to build a straight from `first` to `first + groupSize - 1`
            for i in range(first, first + groupSize):
                if i not in count:  # missing a needed consecutive card
                    return False

                count[i] -= 1

                # If count reaches 0, remove it from min-heap
                if count[i] == 0:
                    # Important rule:
                    # The ONLY card that can disappear from the heap is the SMALLEST
                    # current card (minH[0]). Otherwise we break sorted order.
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)

        # If all cards have been grouped successfully
        return True


"""
-------------------- 🔎 DETAILED DRY RUN --------------------

hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Count Map → {1:1, 2:2, 3:2, 4:1, 6:1, 7:1, 8:1}
Min-heap → [1,2,3,4,6,7,8]

Iteration 1:
  Start from smallest → 1
  Need → 1,2,3
  After decreasing:
      count = {1:0, 2:1, 3:1, 4:1, 6:1, 7:1, 8:1}
  Pop 1 from heap (because count=0)

Iteration 2:
  Start from next smallest → 2
  Need → 2,3,4
  After decreasing:
      count = {2:0, 3:0, 4:0, 6:1, 7:1, 8:1}
  Pop 2 → pop 3 → pop 4

Iteration 3:
  Start from next smallest → 6
  Need → 6,7,8
  After decreasing:
      all become count 0
  Pop 6 → pop 7 → pop 8

Heap becomes empty → return True

-------------------- ⚙️ WHY GREEDY SOLUTION IS CORRECT --------------------

✓ The smallest card must always start a straight — it cannot be inserted into
  the middle of any other straight because no smaller card exists before it.

✓ If the smallest card cannot form a valid straight, the entire hand cannot be
  partitioned — so early return False is valid.

✓ We remove cards from heap strictly in increasing order — guaranteeing we do not
  violate sorted consecutive structure.

Time Complexity:  O(n log n) — due to heap operations
Space Complexity: O(n)

"""
