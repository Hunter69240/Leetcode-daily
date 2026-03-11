def s():
    version1 = "1.0.1"
    version2 = "1"

    # ---------------------------------------------------------
    # EXPLANATION:
    # We compare two version numbers.
    #
    # Steps:
    # 1) Split versions by "." to get each revision.
    # 2) Convert each revision to integer (to ignore leading zeros).
    # 3) Pad the shorter version with zeros so both have same length.
    # 4) Compare revisions one by one:
    #    - if version1 > version2 → return 1
    #    - if version1 < version2 → return -1
    #    - if equal → continue
    # 5) If all revisions equal → return 0
    # ---------------------------------------------------------

    resa = version1.split(".")
    resb = version2.split(".")

    # Convert all parts to integers
    for i in range(len(resa)):
        resa[i] = int(resa[i])

    for i in range(len(resb)):
        resb[i] = int(resb[i])

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # version1 = "1.0.1" → resa = [1, 0, 1]
    # version2 = "1"     → resb = [1]
    #
    # length = max(3,1) = 3
    #
    # Pad shorter list with zeros:
    # resa = [1,0,1]
    # resb = [1,0,0]
    # ---------------------------------------------------------

    length = max(len(resa), len(resb))
    if len(resa) < length:
        resa += [0] * (length - len(resa))
    else:
        resb += [0] * (length - len(resb))

    i, j = 0, 0

    # ---------------------------------------------------------
    # COMPARISON DRY RUN:
    #
    # i=0:
    #   resa[0]=1, resb[0]=1 → equal → continue
    #
    # i=1:
    #   resa[1]=0, resb[1]=0 → equal → continue
    #
    # i=2:
    #   resa[2]=1, resb[2]=0
    #   resa > resb → return 1
    # ---------------------------------------------------------

    while i < len(resa) and j < len(resb):
        if resa[i] > resb[j]:
            return 1
        elif resa[i] < resb[j]:
            return -1
        i += 1
        j += 1

    # All revisions equal
    return 0


a = s()
print(a)
