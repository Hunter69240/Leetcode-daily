def s():
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    i = j = 0
    result = []

    # ---------------------------------------------------------
    # EXPLANATION:
    # We are finding intersections between two lists of intervals.
    #
    # Both lists are sorted and non-overlapping internally.
    #
    # Use two pointers:
    #   i → pointer for firstList
    #   j → pointer for secondList
    #
    # For each pair of intervals:
    #   - Overlap start = max(start times)
    #   - Overlap end   = min(end times)
    #
    # If start <= end → valid intersection
    #
    # Then move the pointer of the interval
    # that ends first (cannot overlap further).
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # firstList  = [[0,2],[5,10],[13,23],[24,25]]
    # secondList = [[1,5],[8,12],[15,24],[25,26]]
    #
    # i=0 → [0,2]
    # j=0 → [1,5]
    #
    # start = max(0,1) = 1
    # end   = min(2,5) = 2
    # 1 <= 2 → append [1,2]
    #
    # aEnd < bEnd → move i
    #
    # ---------------------------------------------------------
    # i=1 → [5,10]
    # j=0 → [1,5]
    #
    # start = max(5,1) = 5
    # end   = min(10,5) = 5
    # append [5,5]
    #
    # bEnd <= aEnd → move j
    #
    # ---------------------------------------------------------
    # i=1 → [5,10]
    # j=1 → [8,12]
    #
    # start = max(5,8) = 8
    # end   = min(10,12) = 10
    # append [8,10]
    #
    # aEnd < bEnd → move i
    #
    # ---------------------------------------------------------
    # i=2 → [13,23]
    # j=1 → [8,12]
    #
    # start = max(13,8) = 13
    # end   = min(23,12) = 12
    # no overlap
    #
    # bEnd < aEnd → move j
    #
    # ---------------------------------------------------------
    # i=2 → [13,23]
    # j=2 → [15,24]
    #
    # start = max(13,15) = 15
    # end   = min(23,24) = 23
    # append [15,23]
    #
    # aEnd < bEnd → move i
    #
    # ---------------------------------------------------------
    # i=3 → [24,25]
    # j=2 → [15,24]
    #
    # start = max(24,15) = 24
    # end   = min(25,24) = 24
    # append [24,24]
    #
    # bEnd <= aEnd → move j
    #
    # ---------------------------------------------------------
    # i=3 → [24,25]
    # j=3 → [25,26]
    #
    # start = max(24,25) = 25
    # end   = min(25,26) = 25
    # append [25,25]
    #
    # aEnd < bEnd → move i
    #
    # i reaches end → stop
    #
    # FINAL RESULT:
    # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    # ---------------------------------------------------------

    while i < len(firstList) and j < len(secondList):
        aStart, aEnd = firstList[i]
        bStart, bEnd = secondList[j]

        # Calculate overlap
        start = max(aStart, bStart)
        end = min(aEnd, bEnd)

        # If intervals overlap, add intersection
        if start <= end:
            result.append([start, end])

        # Move the pointer of the interval that ends first
        if aEnd < bEnd:
            i += 1
        else:
            j += 1

    return result


a = s()
print(a)
