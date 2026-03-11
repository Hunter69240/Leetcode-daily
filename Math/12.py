def a():
    # Given integer to convert into Roman numeral
    num = 3749

    # List of (value, symbol) pairs in descending order
    # Includes subtractive cases like 900 (CM), 4 (IV), etc.
    values = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I")
    ]

    # Result string to store the Roman numeral
    result = ""

    # Traverse each value-symbol pair
    for value, symbol in values:
        # Append the symbol while the number is large enough
        while num >= value:
            result += symbol
            num -= value

    # Return the final Roman numeral string
    return result
