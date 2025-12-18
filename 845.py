arr = [2, 1, 4, 7, 3, 2, 1, 0, 5]

up = [0 for i in range(len(arr))]
down = [0 for i in range(len(arr))]
res = 0

# ---------------------------------------------------------
# EXPLANATION:
# This code finds the length of the LONGEST MOUNTAIN in array.
#
# A mountain:
#   - strictly increasing
#   - then strictly decreasing
#   - length >= 3
#
# up[i]   → length of increasing sequence ending at i
# down[i] → length of decreasing sequence starting at i
#
# A valid mountain peak at index i requires:
#   up[i] > 0 and down[i] > 0
#
# Mountain length at i:
#   up[i] + down[i] + 1
# ---------------------------------------------------------

# ---------------------------------------------------------
# FIRST PASS: BUILD `up` ARRAY
# up[i] = how many steps increasing ending at index i
#
# DRY RUN:
#
# arr = [2,1,4,7,3,2,1,0,5]
#
# i=1: 1 < 2 → no increase → up[1]=0
# i=2: 4 > 1 → up[2]=1
# i=3: 7 > 4 → up[3]=2
# i=4: 3 < 7 → up[4]=0
# i=5: 2 < 3 → up[5]=0
# i=6: 1 < 2 → up[6]=0
# i=7: 0 < 1 → up[7]=0
# i=8: 5 > 0 → up[8]=1
#
# up = [0,0,1,2,0,0,0,0,1]
# ---------------------------------------------------------

for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        up[i] = up[i - 1] + 1


# ---------------------------------------------------------
# SECOND PASS: BUILD `down` ARRAY
# down[i] = how many steps decreasing starting at index i
#
# DRY RUN:
#
# i=7: 0 < 5 → no decrease → down[7]=0
# i=6: 1 > 0 → down[6]=1
# i=5: 2 > 1 → down[5]=2
# i=4: 3 > 2 → down[4]=3
# i=3: 7 > 3 → down[3]=4
# i=2: 4 < 7 → down[2]=0
# i=1: 1 < 4 → down[1]=0
# i=0: 2 > 1 → down[0]=1
#
# down = [1,0,0,4,3,2,1,0,0]
# ---------------------------------------------------------

for i in range(len(arr) - 2, -1, -1):
    if arr[i] > arr[i + 1]:
        down[i] = down[i + 1] + 1


# ---------------------------------------------------------
# FINAL PASS: FIND LONGEST MOUNTAIN
#
# Check each index i:
# if up[i] > 0 and down[i] > 0 → valid peak
#
# DRY RUN:
#
# i=3:
#   up[3]=2, down[3]=4
#   mountain length = 2 + 4 + 1 = 7
#
# This is the longest mountain.
# ---------------------------------------------------------

for i in range(len(arr)):
    if up[i] > 0 and down[i] > 0:
        res = max(res, up[i] + down[i] + 1)

print(up)
print(down)
print(res)
