class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        ---------------------------------------------------------------------------
        📌 PROBLEM TYPE & WHY
        ---------------------------------------------------------------------------
        This is a greedy interval partitioning/string partitioning problem
        (LeetCode – Partition Labels).
        The task is to split the string into the maximum number of partitions such
        that no character appears in more than one partition.

        ---------------------------------------------------------------------------
        💡 INTUITION
        ---------------------------------------------------------------------------
        • Every character has a last position in the string.
        • While iterating from left to right, we keep track of the farthest last
          occurrence of all characters inside the current partition.
        • When our current index reaches that farthest last occurrence, we know:
          → The current partition contains all occurrences of its chars.
          → So we can "cut" the partition and start a new one.
        • We record the size of each partition.

        ---------------------------------------------------------------------------
        🔍 HOW THE CODE WORKS (LINE BY LINE)
        ---------------------------------------------------------------------------
        lastIndex = {}                   → dictionary mapping character → last index
        for i, c in enumerate(s):        → loop to fill lastIndex
            lastIndex[c] = i             → update character’s last seen position

        res = []                         → list to store partition sizes
        size, end = 0, 0                 → size = current partition length
                                           end  = farthest last occurrence seen so far

        for i, c in enumerate(s):        → iterate again through string
            size += 1                    → include character in partition
            end = max(end, lastIndex[c]) → update farthest index for any char inside partition

            if i == end:                 → if we reached the farthest occurrence
                res.append(size)         → record size of partition
                size = 0                 → reset size for next partition

        return res                       → return list of partition sizes

        ---------------------------------------------------------------------------
        🧪 DRY RUN EXAMPLE
        ---------------------------------------------------------------------------
        Input: "ababcbacadefegdehijhklij"

        First pass (build lastIndex):
        lastIndex = {
            a:8, b:5, c:7, d:14, e:15, f:11, g:13, h:19,
            i:22, j:23, k:20, l:21
        }

        Second pass:
        i=0 'a': size=1, end=max(0,8)=8
        i=1 'b': size=2, end=max(8,5)=8
        i=2 'a': size=3, end=8
        i=3 'b': size=4, end=8
        i=4 'c': size=5, end=max(8,7)=8
        i=5 'b': size=6, end=8
        i=6 'a': size=7, end=8
        i=7 'c': size=8, end=8
        i=8 'a': size=9, end=8 → i == end → append 9 → res=[9], size=0

        Continue similarly...
        Next partitions result: 7 and 8

        Final result: [9, 7, 8]

        ---------------------------------------------------------------------------
        END SUMMARY
        ---------------------------------------------------------------------------
        ✔ We track each character’s last position
        ✔ Expand current partition to include all its characters' occurrences
        ✔ When index equals partition end → close partition
        ✔ Output partition sizes
        ---------------------------------------------------------------------------
        '''

        lastIndex = {}  # char -> last index in string
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res
