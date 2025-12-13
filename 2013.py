class DetectSquares:

    def __init__(self):
        # ---------------------------------------------------------
        # EXPLANATION:
        # ptsCount → counts how many times a point (x, y) was added
        # pts      → list of all points added (keeps duplicates)
        #
        # ptsCount is used for O(1) lookup of how many times
        # a specific point exists.
        # ---------------------------------------------------------
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        # ---------------------------------------------------------
        # EXPLANATION:
        # Every time a point is added:
        # - increment its count in ptsCount
        # - append it to pts list
        # ---------------------------------------------------------
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

        # DRY RUN (add):
        # add([3, 10])
        # ptsCount = {(3,10):1}
        # pts = [[3,10]]

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        # ---------------------------------------------------------
        # EXPLANATION:
        # We treat `point` as one corner of a square.
        #
        # For every previously added point (x, y):
        #   - it can be a diagonal corner of the square only if:
        #       1) |px - x| == |py - y|   (equal side length)
        #       2) x != px and y != py    (not same row or column)
        #
        # If valid diagonal:
        #   the other two required points are:
        #       (x, py) and (px, y)
        #
        # Number of squares formed:
        #   ptsCount[(x, py)] * ptsCount[(px, y)]
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        #
        # Points added:
        #   add([3,10])
        #   add([11,2])
        #   add([3,2])
        #
        # count([11,10])
        #
        # px=11, py=10
        #
        # Loop over pts:
        #
        # 1) (x,y) = (3,10)
        #    |10-10| != |11-3| → skip
        #
        # 2) (x,y) = (11,2)
        #    |10-2| != |11-11| → skip
        #
        # 3) (x,y) = (3,2)
        #    |10-2| == |11-3| == 8  ✔
        #    x!=px and y!=py ✔
        #
        #    Other points needed:
        #       (3,10) and (11,2)
        #
        #    res += ptsCount[(3,10)] * ptsCount[(11,2)]
        #        = 1 * 1 = 1
        #
        # FINAL RESULT = 1 square
        # ---------------------------------------------------------

        for x, y in self.pts:
            # Check diagonal validity
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            # Count squares using the other two corners
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res


# ---------------------------------------------------------
# USAGE DRY RUN:
#
# obj = DetectSquares()
# obj.add([3,10])
# obj.add([11,2])
# obj.add([3,2])
#
# obj.count([11,10]) → 1
# ---------------------------------------------------------
