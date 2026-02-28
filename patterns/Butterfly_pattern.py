'''
Docstring for patterns.Butterfly_pattern

*      *
**    **
***  ***
********
********
***  **
**    **
*      *
'''

n = 4

# Total rows = 2 * n
# Because butterfly has upper half + lower half
for i in range(2 * n):

    # -------------------------------------------------
    # THINKING LOGIC FOR STARS
    # -------------------------------------------------
    # If we convert pattern to numbers (left stars):
    # 1 2 3 4 4 3 2 1
    #
    # First half (i < n):
    #   stars increase → stars = i + 1
    #
    # Second half (i >= n):
    #   stars decrease → stars = 2*n - i
    #
    # Why 2*n - i?
    # Total rows = 2*n
    # When i = 4 → 8 - 4 = 4
    # When i = 5 → 8 - 5 = 3
    # When i = 6 → 8 - 6 = 2
    # When i = 7 → 8 - 7 = 1
    #
    # So it mirrors perfectly.

    if i < n:
        stars = i + 1
        # Spaces shrink as stars grow
        # For upper half:
        # spaces = 2*(n - i - 1)
    else:
        stars = 2 * n - i
        # For lower half:
        # spaces grow again

    # -------------------------------------------------
    # THINKING LOGIC FOR SPACES
    # -------------------------------------------------
    # Maximum width occurs at middle row:
    # **** ****
    # 4 + 4 = 8 = 2*n
    #
    # Every row prints:
    # left stars + right stars = 2*stars
    #
    # So remaining width becomes spaces:
    # spaces = total_width - 2*stars
    # spaces = 2*n - 2*stars

    spaces = 2 * n - 2 * stars

    # left stars
    for s in range(stars):
        print("*", end="")

    # middle spaces
    for sp in range(spaces):
        print(" ", end="")

    # right stars
    for s in range(stars):
        print("*", end="")

    print()